import pytest
from bank import value



def test_hello():
    assert value("hello")==0
def test_h_letter():
    assert value("h")==20
def test_nothing():
    assert value("finish")==100

def test_case_insensitivity():
    assert value("H")==20


def test_phrase():
    assert value("hello,do you want to ")==0
