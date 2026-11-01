def main():
    text = input("What time is it ? ")
    if 7 <= convert(text) <= 8: 
      print("breakfast time")
    elif 12 <= convert(text) <= 13:
      print("lunch time")
    elif 18 <= convert(text) <= 19:
      print("dinner time")


def convert(time):
    h, m = time.split(":")
    h, m = int(h), int(m)

    return float(h + (m / 60))
    


if __name__ == "__main__":
    main()
