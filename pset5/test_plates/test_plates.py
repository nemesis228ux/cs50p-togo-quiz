from plates import is_valid

def test_valid():
    assert is_valid("AA") == True
    assert is_valid("AAA123") == True
    assert is_valid("CS50") == True


def test_too_short_or_long():
    assert is_valid("A") == False       
    assert is_valid("AAAAAAA") == False 


def test_must_start_with_two_letters():
    assert is_valid("5B") == False
    assert is_valid("C2") == False    


def test_no_zero_as_first_digit():
    assert is_valid("CS05") == False
    assert is_valid("CC01") == False


def test_no_letters_after_digits():
    assert is_valid("AA1B") == False
    assert is_valid("CS50P") == False


def test_no_punctuation_or_spaces():
    assert is_valid("BB !") == False
    assert is_valid("AA.BB") == False