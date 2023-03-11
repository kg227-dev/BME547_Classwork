import requests

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/kg227")
print(r.text)


patient1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M7")
print(patient1.text)

patient2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F1")
print(patient2.text)

out_data = {"Name": "kg227", "Match":  "No"}

r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)

print(r.status_code)
print(r.text)
