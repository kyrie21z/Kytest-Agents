"""模型命令的文件及网络边界；隔离不可用时拒绝执行，不回落到宿主机。"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Sequence


class SandboxUnavailable(ValueError):
    pass


def sandbox_command(
    argv: Sequence[str], *, workspace: Path, cwd: Path, allow_write: bool
) -> List[str]:
    """Linux Bubblewrap：工作区 + 只读系统/Python 运行库 + 私有临时目录。

    运行库属于明确允许的工作区外路径。不会挂载整个 /、/home、/mnt 或
    宿主机 /tmp；不会继承宿主机网络、PID 命名空间或可提升权限的能力。
    """
    executable = shutil.which("bwrap") if sys.platform == "linux" else None
    if not executable:
        raise SandboxUnavailable(
            "命令隔离不可用：需要 Linux 和 Bubblewrap（bwrap）。"
            "命令未执行；仅对受信代码可显式选择 --execution-mode trusted。"
        )

    roots = [Path(p) for p in ("/usr", "/bin", "/lib", "/lib64") if Path(p).exists()]
    # Python/venv 的依赖必须能加载，只暴露这两个实际安装目录。
    for prefix in (sys.base_prefix, sys.prefix):
        root = Path(prefix).resolve()
        if not any(root == p or p in root.parents for p in roots):
            roots.append(root)
    workspace = workspace.resolve()
    for root in roots:
        if workspace == root or workspace in root.parents or root in workspace.parents:
            raise SandboxUnavailable("工作区与只读运行库重叠，请使用独立的项目目录。")

    command = [
        executable, "--unshare-all", "--die-with-parent", "--new-session",
        "--cap-drop", "ALL", "--proc", "/proc", "--dev", "/dev",
        "--tmpfs", "/tmp", "--tmpfs", "/run",
    ]
    for root in roots:
        command.extend(["--ro-bind", str(root), str(root)])
    # 解释器路径上的符号链接（如 uv 的 cpython-3.12-… -> cpython-3.12.15-…）
    # 不在上面挂载的实际目录里，按原样在隔离内重建，否则 venv 的 python 找不到。
    for link, target in interpreter_links(roots).items():
        command.extend(["--symlink", target, str(link)])
    for filename in ("/etc/ld.so.cache", "/etc/localtime"):
        if Path(filename).exists():
            command.extend(["--ro-bind", filename, filename])
    command.extend([
        "--bind" if allow_write else "--ro-bind", str(workspace), str(workspace),
        "--chdir", str(cwd), "--setenv", "HOME", "/tmp",
        "--setenv", "TMPDIR", "/tmp", "--", *argv,
    ])
    return command


def interpreter_links(roots: Sequence[Path]) -> dict:
    """从 sys.executable 和 Python 前缀出发，沿符号链接链收集挂载目录之外的链接。"""
    links = {}
    for start in (sys.executable, sys.prefix, sys.base_prefix):
        path = Path(os.path.abspath(start))
        for _ in range(40):  # 链长上限，防止环
            for part in (path, *path.parents):
                if part.is_symlink() and not any(part == r or r in part.parents for r in roots):
                    links[part] = os.readlink(part)
            if not path.is_symlink():
                break
            target = Path(os.readlink(path))
            path = Path(os.path.abspath(target if target.is_absolute() else path.parent / target))
    return links


def sandbox_preflight(base: Path) -> str:
    """在 base 下的临时工作区里隔离启动一次当前解释器；失败时返回原因，成功返回空串。"""
    base.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=base, prefix=".preflight-") as tmp:
        workspace = Path(tmp)
        try:
            argv = sandbox_command([sys.executable, "-c", "pass"], workspace=workspace, cwd=workspace, allow_write=False)
        except SandboxUnavailable as exc:
            return str(exc)
        result = subprocess.run(argv, capture_output=True, text=True, timeout=30)
        return "" if result.returncode == 0 else (result.stderr.strip() or f"exit {result.returncode}")
