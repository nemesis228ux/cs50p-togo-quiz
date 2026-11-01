expression = input("Expression: ")

x, y, z = expression.split(" ")

x = int(x)
z = int(z)

match y:
  case "+":
    result = x + z
  case "-":
    result = x - z
  case "*":
    result = x * z
  case "/":
    result = x / z

print(f"{float(result):.1f}")