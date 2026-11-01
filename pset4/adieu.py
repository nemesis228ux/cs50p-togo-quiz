import inflect

p = inflect.engine()

names = []

while True:
  try:

    name = input("Name: ")
    names.append(name.strip())

  except EOFError:
    print(f"\nAdieu, adieu, to {p.join(names)}")
    break