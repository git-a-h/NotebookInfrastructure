from src.step_1.dummy_add import add


def test_add_integers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_add_floats():
    assert add(2.5, 2.5) - 5.0 < 1e-9


def test_add_complex():
    assert add(1 + 2j, 3 + 4j) == 4 + 6j
