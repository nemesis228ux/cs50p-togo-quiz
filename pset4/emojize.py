from emoji import emojize

data = input("Input : ")

print(emojize(data.strip(), language='alias'))