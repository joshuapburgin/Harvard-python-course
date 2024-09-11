import pytest
from seasons import calc_minutes



def test_normal():
    assert calc_minutes("2001-02-13")=="Twelve million, one hundred seventy-three thousand, seven hundred sixty minutes"
    



