def main():
  user_input = input("Input: ")
  print(shorten(user_input), end="")


def shorten(word: str):
  result = ""
  for char in word:
    if char not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
      result += char

  return result


if __name__ == "__main__":
    main()