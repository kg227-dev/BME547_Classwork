import logging
from flask import Flask, request, jsonify

"""
Database Description: A dictionary of dictionaries.
keys -> ids for the patients
values -> Dictionary with patient information
Patient dictionary will look like this example:
  {"id": 1, "name": "David", "blood_type": "O+", "tests": []}
The "tests" list will be a series of tuples that contain the test
name and test result
"""

#create global variable to hold database
db = {}

#create an instance of the Flask server
app = Flask(__name__)

def add_patient_to_db(id, name, blood_type):
    """ Adds a new patient dictionary to the database
    This function receives basic information on a new patient, creates a
    dictionary containing that information, as well as an empty list to hold
    test data to be added in the future, and adds this patient dictionary to
    the database dictionary using the patient id as a key.
    The database is being stored in an internal global variable.  As this
    variable is a dictionary that has already been created, and a dictionary
    is a mutable data type, the use of the "global" keyword is not required.
    The function also prints the database to the console so that we can see
    how the database is changing as the server is being used.
    Args:
        patient_id (int): The medical record number of the patient
        patient_name (str): Full name of patient
        blood_type (str): Blood type of the patient
    Returns:
        None
    """
    new_patient = {"id" : id,
                   "name" : name, 
                   "blood_type" : blood_type,
                   "tests": []}
    
    db[id] = new_patient

@app.route("/new_patient", methods = ["POST"])
def post_new_patient():
    #Get input data 
    in_data = request.get_json()    
    #Call other functions to do the work 
    answer, status_code = new_patient_driver(in_data)
    #Return a response
    return jsonify(answer), status_code

def new_patient_driver(in_data):
    #Validate input     
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400
    #Do the work 
    add_patient_to_db(in_data["id"], in_data['name'], in_data['blood_type'])
    #Return an answer 
    return "Patient successfully added", 200

@app.route("/add_test", methods = ["POST"])
def post_add_test()
    #Get input data
    in_data = request.get_json()
    answer, status_code = add_test_driver(in_data)
    return jsonify(answer), status_code


def add_test_to_db(id, test_name, test_result):
    db[id]["test"]
    return

def does_patient_exist_

def add_test_driver(in_data):
    validation = validate_input_data_add_test(in_data)
    if validation is not True:
        return validation, 400
    does_id_exist = does_patient_exist_in_db(in_data['ID'])
    if does_id_exist is False:
        return "Patient id {} does not exist in database"\
        .format(in_data[id], 400)
    

def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value_type".format(key)
    return True

def validate_input_data_add_test(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value_type".format(key)
    return True

if __name__ == "__main__":
    app.run()

