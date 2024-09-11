import requests
import sys
import json

try:
    if len(sys.argv)!=2:
        raise ValueError("Missing command-line argument")

    try:
        bitcoin_number=float(sys.argv[1])
    except ValueError:
        raise ValueError("Command-line argument is not a number")

    call_object= requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")


    price = call_object.json()['bpi']['USD']['rate_float']
    total_value=price*bitcoin_number

    formatted_value=f"${format(total_value,',.4f')}"



    print(formatted_value)

except ValueError as e:
    print(e)
    sys.exit(1)


except requests.RequestException:
    print("API call did not work")

