import sys
import requests
import json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) == 2:
    try:
        x = float(sys.argv[1])
    except ValueError:
        sys.exit("command-line argument is not a number")

    response =  requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    y = response.json()
    z = y['bpi']['USD']['rate']
    c = z.replace(',','')
    print(f'${x*float(c):,.4f}')
