
import pytest
import os
from LinearRegression.LinearRegression import LinearRegression

SCOPE = "function"

global current
current = 0


@pytest.fixture(scope=SCOPE)
def shared_instance():
    global current
    current = LinearRegression([0], [0])
    yield current

# TODO: Add a list of datasets for testing purposes.
# http://people.sc.fsu.edu/~jburkardt/datasets/regression/regression.html

# TODO: Add test-cases to all units


@pytest.mark.parametrize(
    'number, word', [
        ([1, 2, 3, 4, 5, 6, 7, 8], [11, 22, 33, 44, 55, 66, 77, 88])
    ]
)
def test_getSlope(number, word, shared_instance):
    shared_instance.setX(number)
    shared_instance.setY(word)
    assert round(shared_instance.getSlope(), 2) == 11


def test_getX(shared_instance):
    assert shared_instance.getX() != 0


def test_getY(shared_instance):
    assert shared_instance.getY() != 0
