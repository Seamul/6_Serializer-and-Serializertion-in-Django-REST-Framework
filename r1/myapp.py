import requests
URL='http://127.0.0.1:8000/studentinfo'
r=requests.get(url=URL)
print(r)
data=r.json()
print(data)