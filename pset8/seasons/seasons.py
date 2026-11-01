from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth = input("Date Of Bith: ")
    year, month, day = get_birth_date(birth)
    user_date = date(year, month, day)
    delta_date = date.today() - user_date
    minutes = delta_date.days * 24 * 60
    print(f"{p.number_to_words(minutes, andword=' ')} minutes".capitalize())

def get_birth_date(birth):
    if matches :=  re.search(r"^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1])$", birth):
        year = matches.group(1)
        month = matches.group(2)
        day = matches.group(3)
        return (int(year),int(month), int(day))
    else:
        sys.exit("Invalid date")
    


if __name__ == "__main__":
    main()