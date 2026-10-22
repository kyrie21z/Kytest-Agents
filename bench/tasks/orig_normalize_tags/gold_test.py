import pytest
from solution import normalize_tags


@pytest.mark.parametrize("text, expected", [
    (" Python, ML ,python,, Data ", ["python", "ml", "data"]),
    ("", []),
    (" , ,, ", []),
    ("a", ["a"]),
    ("b,a,B,c,A", ["b", "a", "c"]),
    ("Zeta, alpha, Mid", ["zeta", "alpha", "mid"]),
    ("x,", ["x"]),
    (",x", ["x"]),
    ("\tTab\t,\nNew\n", ["tab", "new"]),
    ("data science, Data Science", ["data science"]),
])
def test_examples(text, expected):
    assert normalize_tags(text) == expected
