import pytest
from twttr import shorten
import string



lower_word_pairs= {"name":"nm" , "hello":"hll" , }
upper_word_pairs= {"NAME":"NM" , "HELLO":"HLL" , }

def test_allvowels():
    assert shorten("aeiouAEIOU")==""

def test_lowercase():
    assert shorten("aeiou")==""

def test_uppercase():
    assert shorten("AEIOU")==""

def test_number():
    assert shorten("1234567890")=="1234567890"

def test_print_in_Uppercase():
    assert shorten("hello")=="hll"

def test_omitting_punctuation():
    assert shorten(string.punctuation)==string.punctuation





