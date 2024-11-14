import pytest

from src.base import factorial


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
