#import math
#
#print(math.pi)
import random
import datetime
import os
import json
import requests

import pandas as pd

from math import sqrt, pi


print(pi)

print(random.randint(1,10))
print(random.choice(['red','black']))

print(datetime.date.today())

print(os.getcwd())

data = {
    'name': 'Camilo',
    'age': 25
}
print(json.dumps(data))

lt = 48.85
lg = 2.36

url = f"https://api.open-meteo.com/v1/forecast?latitude={lt}&longitude={lg}&current=temperature_2m"

reponse = requests.get(url)
data = reponse.json()

print(data)