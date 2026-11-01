amount_due = 50
change_owed = 0
while amount_due != 0:
  print(f"Amount Due: {amount_due}")
  given = int(input("Insert Coin: "))
  if given != 50 and given in [25, 10, 5]:
    if given > amount_due:
      change_owed = given - amount_due
      amount_due -= amount_due
    else:
      amount_due -= given
print("Change Owed:",change_owed)