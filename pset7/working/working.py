import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)",
        s
    )
    if not match:
        raise ValueError("Invalid format")

    h1, m1, period1, h2, m2, period2 = match.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not (0 <= m1 <= 59 and 0 <= m2 <= 59):
        raise ValueError("Invalid format")
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError("Invalid format")

    h1 = convert_to24(h1, period1)
    h2 = convert_to24(h2, period2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

def convert_to24(hour, period):
    if period == "AM":
        return 0 if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12

if __name__ == "__main__":
    main()