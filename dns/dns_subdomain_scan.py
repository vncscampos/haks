#!/usr/bin/python3

import requests
import json

domain = input('Digite o domínio: ')

crt = 'https://crt.sh/?q='+ domain +'&output=json'

try:
    response = json.loads(requests.get(crt).text)
    for obj in response:
        print(obj['common_name'])
        print(obj['name_value'])
        print('\n')
except Exception as err:
    print(err)