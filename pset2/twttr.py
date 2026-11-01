def main():
  user_input = input("Input: ")
  print(twttr(user_input), end="")


def twttr(text: str):
  word = ""
  for char in text:
    if char not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
      word += char

  return word


main()