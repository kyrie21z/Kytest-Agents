"""Public specification of a module: what the Planner is allowed to see.

Keeps imports, signatures, decorators and docstrings; drops every function and
method body, class-level assignments and module-level code. The Planner must
work out expected behaviour from the specification alone, so an implementation
bug cannot leak into the plan.
"""
from __future__ import annotations

import ast

_HIDDEN = ast.Expr(ast.Constant(...))


def _strip_function(node):
    doc = ast.get_docstring(node, clean=False)
    node.body = ([ast.Expr(ast.Constant(doc))] if doc else []) + [_HIDDEN]
    return node


def _strip_class(node):
    body = []
    doc = ast.get_docstring(node, clean=False)
    if doc:
        body.append(ast.Expr(ast.Constant(doc)))
    for child in node.body:
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
            body.append(_strip_function(child))
        elif isinstance(child, ast.ClassDef):
            body.append(_strip_class(child))
    node.body = body or [_HIDDEN]
    return node


def extract_spec(source: str) -> str:
    tree = ast.parse(source)
    kept = []
    for i, node in enumerate(tree.body):
        if i == 0 and isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, str):
            kept.append(node)  # module docstring
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            kept.append(node)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            kept.append(_strip_function(node))
        elif isinstance(node, ast.ClassDef):
            kept.append(_strip_class(node))
    tree.body = kept
    return ast.unparse(tree) + "\n"
