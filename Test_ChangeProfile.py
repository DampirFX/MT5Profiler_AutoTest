import pytest
from Cases import *


def test_wrong_request():
    assert wrong_request() == 'result - OK'