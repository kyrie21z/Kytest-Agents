# Homework 2 范围：Kytest-Agents

截止 2026-10-25 24:00。在 Homework 1（Kytest-Agent，单 Agent 测试生成）之上做增量：
把"先理解规格、再写测试、执行验证、复核裁决"拆成多个 Agent，并为整个 MAS 设计新基准。

## 要回答的问题

测试的价值在于区分对错。单 Agent 读完实现再写断言，预期值容易从实现里抄来；
被测代码本身有 bug 时，这样的测试会把 bug 固化成"正确"。H1 的 `submit_tests`
只保留在被测实现上通过的测试，在有 bug 的实现上恰好会丢掉正确的测试。

## 工作流

| 节点 | LLM | 输入 | 输出 |
|---|---|---|---|
| Planner | 是 | 只有规格：签名、docstring、任务说明（函数体被剥离） | 测试计划：带编号的条目（类别、输入、预期行为与依据、置信度） |
| TestGen | 是（复用 H1 A4 Agent） | 计划 + 完整源码 | 候选测试，每条引用计划编号 |
| Verifier | 否 | 候选测试 | 在被测实现上的通过/失败、覆盖率、变异得分 |
| Reviewer | 是 | 计划、失败的测试与诊断、覆盖与存活变异 | 对每个失败裁决"测试错"或"疑似实现缺陷"；决定 accept / revise |

- 控制流：Planner → TestGen → Verifier → Reviewer；Reviewer 判 revise 且轮次 < 2 时回到 TestGen，
  否则结束（accepted / forced）。不可恢复错误进入 failed 分支。全部写在一张转移表里，不用框架。
- 产物：`test_solution.py`（在实现上通过的测试）、`test_suspected_bugs.py`（Reviewer 判为
  "疑似实现缺陷"的测试）、`bug_report.md`、`plan.json`、`state.json`、`log.jsonl`。
- 离线：`--mock` 场景驱动每条分支（一次通过 / 修订回路 / 达到轮次上限 / 发现缺陷 / 失败恢复）。

## 基准（MAS 级）

每题：规格、正确参考实现、隐藏金标准测试，以及仅评测器可见的 bug 变体与合法替代实现。

| 来源 | 题数 | 层 | bug 变体 |
|---|---|---|---|
| BigCodeBench-Hard（Apache-2.0） | 4 | T2 规格丰富的函数 | 手写，标注 synthetic |
| ClassEval（代码 MIT，数据 CC-BY-NC-4.0） | 4 | T3 有状态类 ×3，T5 规格含糊 ×1 | 手写，标注 synthetic |
| QuixBugs（MIT） | 3 | T2 算法 | 自带人写缺陷 |
| BugsInPy（youtube-dl `match_str`） | 1 | T4 模块 | 真实缺陷；时间不够最先砍 |
| 原创 | 2 | T5 ×1、未公开对照 ×1 | 手写 |

- 划分：开发集 5 题用于调提示词；测试集 9 题冻结，不在测试集上调参。
- 合法替代实现：每题 1–2 个，必须通过官方测试。
- 配置：H1-A0、H1-A4、MAS-full、MAS−Planner、MAS−Reviewer；每配置 2 次重复。
- 指标：有效率；bug 变体检出率；合法替代实现上的误报率；抗污染检出（被测对象换成 bug 变体时，
  MAS 是否把该缺陷报告出来）；计划要点覆盖；计划→测试引用率；每轮收益；token/调用/耗时。
- 小样本只做描述性报告并附区间，不声称显著性。来源与许可证逐题记录在 `THIRD_PARTY.md`。

## 优先级

P0 工作流 + 离线演示 + 测试 + README/Design.md → P1 基准 14 题与运行 → P2 扩题与重复。

## 不做

多语言、仓库级任务、Docker 环境、框架（LangGraph 等）、并行 Agent、新的 Web UI。
