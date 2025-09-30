"""Tests for multiply()."""
from calculator import multiply

def test_multiply_basic():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(9, 0) == 0
