in_file = open("BME547_Classwork/input_file.txt", "r")
first_line = in_file.readline()
patient_data = first_line.strip("\n").split("=")
patient_id = int(patient_data[1])
