def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    is_valid = True
    found_number = False
    number = ""

    if not validate_before_loop(s):
        return False

    for c in s:
        if not c.isdigit() and not c.isalpha():
            is_valid = False
            break
        if c.isalpha():
          if found_number:
            is_valid = False
          else:
              is_valid = True
        if c.isdigit():
            number += c
            found_number = True


    if number.startswith("0"):
        is_valid = False
            

    return is_valid    


def validate_before_loop(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s.isdigit():
        return False

    if s[:2].isalpha():
        return True
        


main()