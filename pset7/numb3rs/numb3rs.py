import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if match is None:
       return False

    for byte in match.groups():
        if not 0 <=  int(byte) <= 255:
          return False

        if len(byte) > 1 and byte[0] == "0":
            return False

    return True
           


if __name__ == "__main__":
    main()