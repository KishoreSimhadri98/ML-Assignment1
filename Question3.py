
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Sisters = ("Amulya", "Shruthi", "Ria", "Anusha", "Sahithi")
Brothers = ("Rakesh", "Vishnu", "Sandeep")
print("Sister names: ", Sisters)
print("Brother names: ", Brothers)

#Join brothers and sisters tuples and assign it to siblings
Siblings = Sisters + Brothers
print("After join brothers and sisters in a tuple: ", Siblings)

#How many siblings do you have?
Count= len(Siblings)
print("Number of Siblings: ", Count)

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Mother = "Chandu"
Father= "Raja"
family_members = list(Siblings)
family_members.append(Father)
family_members.append(Mother)
family_members=tuple(family_members)
print("After appending father and mother name: ", family_members)
