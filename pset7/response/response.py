from validators import email, ValidationError


def main():
  email = input("What's your email address? ")
  print("Valid") if is_valid(email) else print("Invalid")

def is_valid(mail: str):
  try:
    return bool(email(mail))
  except ValidationError:
    return False


if __name__ == "__main__":
  main()