"""Tests for add()."""
from calculator import add

def test_add_basic():
    assert add(2, 3) == 5

def test_add_negatives():
    assert add(-2, -3) == -5
