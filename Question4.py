IT_Companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
Age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print("The length of set is:", len(IT_Companies))

#Add 'Twitter' to it_companies
IT_Companies.add("Twitter")
print(IT_Companies)

#Insert multiple IT companies at once to the set it_companies
Multiple_ITcompanies= ["Tesla","Samsung", "Deloitte", "Meta"]
IT_Companies.update(Multiple_ITcompanies)
print(IT_Companies)

#Remove one of the companies from the set it_companies
IT_Companies.remove("Samsung")
print(IT_Companies)

#What is the difference between remove and discard
#Remove: If the item to remove does not exist, remove() will raise an error
#Discard: If the item to remove does not exist, discard() will NOT raise an error

#Join A and B
C = A.union(B)
print("After joining A and B: ", C)

#Find A intersection B
D = A.intersection(B)
print("After intersecting A and B: ", D)

#Is A subset of B
E = A.issubset(B)
print("Is A subset of B?", E)

#Are A and B disjoint sets
F = A.isdisjoint(B)
print("Are A and B disjoint sets? ", F)

#Join A with B and B with A
G = B.union(A)
print("After joining A With B: ",C, "and joining B with A: ",G)

#What is the symmetric difference between A and B
H = A.symmetric_difference(B)
print("Symmetric difference between A and B:", H)

#Delete the sets completely
del A,B
#print(B)

#Convert the ages to a set and compare the length of the list and the set
I = set(Age)
print("Is length of list and set is same :", len(I)==len(Age))