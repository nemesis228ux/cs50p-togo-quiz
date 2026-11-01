def main():
  x, y = get_fraction("Fraction: ")

  try:
    p = x/y
    p = p * 100
    if p >= 99: 
      print("F")
    elif p <= 1:
      print("E")
    else:
      print(f"{round(p)}%")
  except ZeroDivisionError:
    pass


def get_fraction(prompt: str):
  while True:
    try:
      fraction = input(prompt)
      x, y = fraction.split("/")
      x, y = int(x), int(y)
      if x < 0 or y < 0 or x > y:
        raise ValueError()
    except ValueError:
      pass      
    else:
      return x, y



main()