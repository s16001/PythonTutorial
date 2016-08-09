""""
import math

#三角関数
angle = 13
h = 8
a = math.sin(math.radians(angle)) * h
b = math.cos(math.radians(angle)) * h

#数値の平方根を取得する
math.sqrt(8**2+13**2)
math.atan(8/13)
math.degrees(math.atan(8/13))
"""
import json
from urllib.request import urlopen

API_URL = "http//weather.livedoor.com/forecast/webservice/json/v1?city=471010"
json_data = ""
with urlopen(API_URL) as response:
    for line in response:
        line = line.decode("UTF-8")
        json_data += line

weather = json.loads(json_data)
print("天気予報(那覇)")
print("{0} 最高気温: {1}度".format(weather['forecasts'][0]['telop'],
                              weather['forecasts'][0]['temperature']['max']['celsius']))
print()

from pprint import pprint
pprint.pprint(weather)