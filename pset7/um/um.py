import re

def main():
    print(count(input("Text: ")))


def count(s: str):
    result = re.findall(r"\bum\b", s, re.IGNORECASE)

    return len(result)


if __name__ == "__main__":
    main()