import pytest

from stuff.accum import Accumulator


@pytest.fixture
def accum():
    return Accumulator()


def test_accumulator_init(accum):
    accum = Accumulator()
    assert accum.count == 0


def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
        accum.count = 10
