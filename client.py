import requests

server = "http://127.0.0.1:5000"

r = requests.get(server+"/info")
print(r.status_code)
print(r.text)