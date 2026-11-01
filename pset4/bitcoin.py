import sys

import requests

def get_number_bitcoin():
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")
    else:
        return n

try:
    n = get_number_bitcoin()
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=d681c3463d971d94a0f44bd94cf3e950009be8b598547c4552c77788ef01edd8")
    json_data = response.json()
    price = float(json_data["data"]["priceUsd"])
except requests.RequestException as e:
    sys.exit("Network error")
else:
    print(f"${n * price:,.4f}")