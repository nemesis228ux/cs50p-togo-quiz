import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
  sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
  sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

if not input_file.endswith((".jpg", ".jpeg", ".png")) and not output_file.endswith((".jpg", ".jpeg", ".png")):
  sys.exit("Invalid input")

if input_file.split(".")[-1] != output_file.split(".")[-1]:
  sys.exit("Input and output have different extensions")

## we define a fixed size for our images
size = (600, 600)

try:
  with Image.open(input_file) as im, Image.open("shirt.png") as shirt:
    im = ImageOps.fit(im, size)
    im = im.convert("RGBA")

    shirt = ImageOps.fit(shirt, size)
    shirt = shirt.convert("RGBA")

    im.paste(shirt, mask=shirt)

    if output_file.split(".")[1] in ["jpg", "jpeg"]:
      im = im.convert("RGB")

    im.save(output_file)
except FileNotFoundError:
   sys.exit("File Not Found")