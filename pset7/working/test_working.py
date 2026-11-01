import pytest
from working import convert

def test_valid():
    assert convert("8 AM to 6 PM") == "08:00 to 18:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("7:30 AM to 8:00 PM") == "07:30 to 20:00"
    assert convert("12 AM to 11 PM") == "00:00 to 23:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_invalid():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")