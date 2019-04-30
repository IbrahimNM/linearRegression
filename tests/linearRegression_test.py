
import pytest
import os
from simpleLinearRegression.LinearRegression import LinearRegression

SCOPE = "function"

global current
current = LinearRegression([0], [0])


@pytest.fixture(scope=SCOPE)
def shared_instance():
    global current
    yield current


@pytest.mark.parametrize(
    'number, word', [
        (1, '1'),
        (3, 'Fizz'),
        (5, 'Buzz'),
        (10, 'Buzz'),
        (15, 'FizzBuzz'),
        (16, '16')
    ]
)

def test_para(number, word):
    assert number is not None


def test_getSlope(shared_instance):
    assert True


def test_getX(shared_instance):
    assert shared_instance.getX() == [0]


def test_getY(shared_instance):
    assert shared_instance.getY() == [0]
