def main():
  camel_case = input("camelCase: ")
  print("_".join(snake_case(camel_case)).lower())
  


def snake_case(text: str):
  elements = []
  word = ""
  for char in text:
    if not char.isupper():
      word += char
    else:
      elements.append(word)
      word = char

  if word:
      elements.append(word)
      
  return elements


main()