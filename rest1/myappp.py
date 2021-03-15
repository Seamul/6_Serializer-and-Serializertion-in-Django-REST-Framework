import requests
URL='http://127.0.0.1:8000/student_info/1'
r=requests.get(url=URL)
print(r)
