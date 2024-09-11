import pytest
from numb3rs import validate



def test_byte():
    assert validate(r"1.")==False
    assert validate(r"1.1")==False
    assert validate(r"1.1.1")==False
    assert validate(r"1.1.1.1")==True
def test_incorrect():
    assert validate(r"255.255.255.255")==True
    assert validate(r"300.1.1.1")==False
    assert validate(r"1.300.1.1")==False
    assert validate(r"1.1.300.1")==False
    assert validate(r"1.1.1.300")==False
def test_word():
    assert validate(r"1cat")==False
