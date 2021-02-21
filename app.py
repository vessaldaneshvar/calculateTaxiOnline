import os
from db import session, Price
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()

def calculate_price(source=(35.674498951295405, 51.3558429479599), dest=(35.79357150721434, 51.49016891913135)):
    data = {
        "points": [
            {
                "lat": source[0],
                "lng": source[1]
            },
            {
                "lat": dest[0],
                "lng": dest[1]
            },
            None
        ],
        "waiting": None,
        "tag": 0,
        "round_trip": False,
        "voucher_code": None,
        "service_types": [
            1,
            3
        ],
        "hurry_price": None,
        "hurry_flag": None
    }
    headers = {
        'authorization' : os.getenv('BearerTokenSnapp'),
        'Content-Type' : 'application/json',
    }
    res = requests.post(
        url = "https://app.snapp.taxi/api/api-base/v2/passenger/newprice/s/6/0",
        data = json.dumps(data),
        headers = headers
    )
    if res.status_code == 200:
        res_data = res.json()
        p = Price(price=res_data['data']['prices'][0]['final'], sourceLat=source[0],sourceLong=source[1], destinationLat=dest[0], destinationLong=dest[1])
        s = session()
        s.add(p)
        s.commit()
    else:
        print("error in get price of taxi")
        print('error text : {}'.format(res.text))


if __name__ == '__main__':
    while True:
        calculate_price()
        time.sleep(120)
