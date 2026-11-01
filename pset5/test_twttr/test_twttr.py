from twttr import shorten

def test_lowercase():
  assert shorten("twitter") == "twttr"
  assert shorten("barry") == "brry"


def test_uppercase():
  assert shorten("TWITTER") == "TWTTR"
  assert shorten("HELLO") == "HLL"
  

def test_numbers():
  assert shorten("cs50") == "cs50"
  assert shorten("h3llo") == "h3ll"


def test_punctuation():
  assert shorten("hello!") == "hll!"
  assert shorten("it's") == "t's"