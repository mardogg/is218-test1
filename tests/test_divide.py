"""Tests for divide()."""
import pytest
from calculator import divide

def test_divide_basic():
    assert divide(8, 2) == 4

def test_divide_float():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
