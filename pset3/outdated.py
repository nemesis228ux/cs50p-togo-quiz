months  = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
  try:

    date = input("Date: ")
    ## program the code with two use case
    ## first case: we have "/" in the user's input
    if "/" in date.strip():
      month, day, year = date.split("/")

      month = int(month)
      day = int(day)
      year = int(year)

      if month < 1 or month > 12:
        raise ValueError()

      if day < 1 or day > 31:
        raise ValueError()

      print(f"{year}-{month:02}-{day:02}")
      break

    else:
    ## second use case, we rather have a "," in the user'sinput
      if "," in date.strip(): 
        
        parts = date.split()
        month, day, year = parts[0].capitalize(), int(parts[1].strip(",")), int(parts[2])

        if day < 1 or day > 31:
          raise ValueError()

        if month not in months:
          raise ValueError()

        print(f"{year}-{(months.index(month)+1):02}-{day:02}")
        break

  except (ValueError, IndexError):
    pass

    
