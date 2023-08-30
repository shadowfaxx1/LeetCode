import urllib.request , urllib.parse , urllib.error
import json
import requests

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=input("enter location ")
    if len(address) < 1 : break
    url =serviceurl+urllib.parse.urlencode(
        {'address':address})
    print('ret', url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('ret', len(data), 'char')
    try : 
        js=json.loads(data)
    except:
        js= None
    if not js or 'status' not in js or js['status']!= 'OK':
        print('======= Failure to Ret =======')
        print(data)
        continue
    print(json.dumps(js,indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    print('lat ', lat ,'lng ', lng)
    print
