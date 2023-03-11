import requests

out_data = {"user": "gmoney", "message": "love sosa"}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)



r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/ku$h")
print(r.text)






