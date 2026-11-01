import random

## small function to get the right level
def get_user_level():
  while True:
    try:
      n = int(input("Level: "))
      if n < 0:
        raise ValueError
    except ValueError:
      pass
    else:
      return n


def main():
  level = get_user_level()

  number = random.randint(1, level)

  while True:
    try:
      guess = int(input("Guess: "))

      if guess <= 0:
        raise ValueError

      if guess < number:
        print("Too small!")
      elif guess > number:
        print("Too large!")
      else:
        print("Just right!")
        break
    except ValueError:
      pass

## calling the main function here !
main()

