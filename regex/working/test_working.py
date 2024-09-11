import pytest
from working import convert


def test_format():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"


def test_valueError():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM  5:00 PM")

