import random
from pyfiglet import Figlet
import sys

figlet = Figlet()

fonts = figlet.getFonts()

user_args = sys.argv[1:] 

if len(user_args) == 0:
  figlet.setFont(font=random.choice(fonts))
elif len(user_args) == 2 and user_args[0] in ["-f", "--font"] and user_args[1] in fonts:
  figlet.setFont(font=user_args[1])
else:
  sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))
