from fuel import convert, gauge
import pytest

def test_percentage():
    assert gauge(25)=="25%"

def test_empty():
    assert gauge(1)=="E"

def test_full():
    assert gauge(99)=="F"

def test_valueError():
    with pytest.raises(ValueError):
        convert("12/10")

def test_demoninator0():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_conversion_calc():
    assert convert("5/10")==50


