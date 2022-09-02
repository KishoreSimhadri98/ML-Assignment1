#Create an empty dictionary called dog
Dog = {}
#Add name, color, breed, legs, age to the dog dictionary
Dog.update({'Name' : 'Bruno','Color' : 'Brown','Breed' : 'Shitzu','Legs' : '4','Age' : '5'})

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Student = {'First_name' : 'Kishore',
           'Last_name' : 'Simhadri',
           'Gender' : 'Male',
           'Age' : '23',
           'Marital status' : 'Unmarried',
           'Skills' : ["C","Java","Python","MySQL"],
           'Country' : 'India',
           'City' : 'Rajahmundry', 'Address' : 'Sai Abhaya Enclave, Sri Ram Nagar, Rajahmundry, 533105'}

#Get the length of the student dictionary
print("Length of the Student dictionary is :", len(Student))

#Get the value of skills and check the data type, it should be a list
print("Skills of the student are :", Student['Skills'])
print("Datatype of the skills is :", type(Student['Skills']))

#Modify the skills values by adding one or two skills
Student['Skills'].extend(["HTML", "Azure Sentinel"])
print("Modified skills in the list are :", Student['Skills'])

#Get the dictionary keys as a list
print("Keys in the student dictionary are :", list(Student.keys()))
#Get the dictionary values as a list
print("values in the student dictionary are :", list(Student.values()))