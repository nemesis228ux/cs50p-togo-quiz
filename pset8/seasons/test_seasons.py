from seasons import get_birth_date
import pytest

def test_valid():
    assert get_birth_date("2006-05-03") == (2006, 5, 3)

def test_invalid_format():
    with pytest.raises(SystemExit):
        get_birth_date("October 4, 1998")

def test_invalid_date():
    with pytest.raises(SystemExit):
        get_birth_date("7582-99-88")