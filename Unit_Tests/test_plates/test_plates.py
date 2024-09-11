from plates import is_valid
import string


def test_two_letters():
    assert is_valid("12")==False
    assert is_valid("AA")==True
    assert is_valid("A1")==False
    assert is_valid("1A")==False

def test_max6letters():
    assert is_valid("hhhhhhh")==False
    assert is_valid("AAAAAA")==True
    assert is_valid("A")==False

def test_numbersatend():
    assert is_valid("AAA222")==True
    assert is_valid("AAA22A")==False

def test_punctuation():
    assert is_valid(" ./?")==False
    assert is_valid("he5!45")==False

def test_zero():
    assert is_valid("he40")==True
    assert is_valid("he04")==False

