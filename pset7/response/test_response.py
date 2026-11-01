from response import is_valid

def test_valid_emails():
  assert is_valid("aliscobarry@gmail.com") == True
  assert is_valid("malan@harvard.edu") == True
  assert is_valid("username@subdomain.harvard.edu") == True


def test_invalid_emails():
  assert is_valid("@gmail.com") == False
  assert is_valid("malan@.edu") == False
  assert is_valid("username@harvard") == False
  assert is_valid("username@@harvard") == False
  assert is_valid("just a string") == False