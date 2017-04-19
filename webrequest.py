import requests

#using
ipdump = requests.get('https://ipinfo.io/json')

if ipdump.status_code != 200:
    raise ApiError(ipdump.status_code)
else:
    ipdata = ipdump.json()
    print("your city is {}" .format(ipdata['city']) )
