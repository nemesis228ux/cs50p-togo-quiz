list = []

while True:
  try:
    item = input("")
    list.append(item)
  except (EOFError, KeyError):
    break

## turn list into tuple to avoid printing doublons
groceries = set(list)
groceries = sorted(groceries)

for g in groceries:
  print(f"{list.count(g)} {str(g).upper()}")