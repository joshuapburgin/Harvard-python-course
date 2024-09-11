from jar import Jar
import pytest


def test_init():
    first_test= Jar()
    assert first_test.capacity==12
    second_test= Jar(5)
    assert second_test.capacity==5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar= Jar()
    jar.deposit(2)
    assert jar.size==2
    jar.deposit(10)
    assert jar.size==12


def test_withdraw():
    jar= Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size==8
    jar.withdraw(4)
    assert jar.size==4

