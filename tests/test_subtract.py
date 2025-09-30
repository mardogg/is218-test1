"""Tests for subtract()."""
from calculator import subtract

def test_subtract_basic():
    assert subtract(5, 2) == 3

def test_subtract_negatives():
    assert subtract(-5, -2) == -3
