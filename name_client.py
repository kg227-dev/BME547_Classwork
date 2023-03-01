import requests

out_data = {"name": "Kush Gulati", "net_id": "kg227",
            "e-mail": "kush.gulati@duke.edu"}

r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)


print(r.status_code)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)

