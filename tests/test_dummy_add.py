from src.step_1 import dummy_add
import pytest

def test_add_integers():
    assert dummy_add.add(2, 3) == 5
    assert dummy_add.add(-1, 1) == 0

def test_add_floats():
    assert dummy_add.add(2.5, 2.5) - 5.0 < 1e-9

def test_add_complex():
    assert dummy_add.add(1+2j, 3+4j) == 4+6j