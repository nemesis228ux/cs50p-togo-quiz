import csv, sys

if len(sys.argv) < 3:
  sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
  sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

if not input_file.endswith(".csv"):
  sys.exit("Not a CSV file")

try:
  with open(input_file) as input_file, open(output_file, "w") as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=['first', 'last', 'house'])
    writer.writeheader()

    for row in reader:
      last, first = row["name"].split(", ")
      writer.writerow({'first': first, 'last': last, 'house': row["house"]})

except FileNotFoundError:
  sys.exit(f"Could not read {input_file}")