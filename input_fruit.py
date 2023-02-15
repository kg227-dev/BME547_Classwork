in_file = open("BME547_Classwork/input_file.txt", "r")
fruits = in_file.readlines()
print(fruits)
in_file.close()

in_file = open("BME547_Classwork/input_file.txt", "r")

first_fruit = in_file.readline()
second_fruit = in_file.readline()
print(first_fruit)