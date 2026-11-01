## Defining the einstein function to handle einstein calculation
def einstein(m):
  c = 300000000 
  E = m * (c * c)
  return E

## The main function
def main():
  m = int(input("m: "))
  print(f"E: {einstein(m)}")


main()