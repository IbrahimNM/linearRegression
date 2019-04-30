
import pytest
import os
from simpleLinearRegression.LinearRegression import LinearRegression

SCOPE = "function"

global current
current = LinearRegression([0],[0])


@pytest.fixture(scope=SCOPE)
def shared_instance():
    global current
    yield current

def test_getSlope(shared_instance):
    assert True

