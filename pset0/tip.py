def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str):
    value = d.strip("$")
    return float(value)


def percent_to_float(p: str):
    value = p.strip("%")
    return float(value) / 100


main()