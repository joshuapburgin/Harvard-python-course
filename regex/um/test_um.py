from um import count
import pytest



def test_word():
    assert count("yummy")==0
    assert count("um")==1
    assert count("um?")==1
    assert count(" um ")==1
    assert count(" UM ")==1
