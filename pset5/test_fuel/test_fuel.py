import pytest
from fuel import convert, gauge


def test_convert_matching():
    assert convert("0/100") == 0
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("100/100") == 100


def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_convert_raises_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_raises_value_error():
    with pytest.raises(ValueError):
        convert("3/1")  
    with pytest.raises(ValueError):
        convert("-1/4") 


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_normal():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(73) == "73%"