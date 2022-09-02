import math
Num = int(input("Number of  students:"))
Lbs=[]
Wts=[]
for i in range(Num):
    Lbs.append(int(input()))
for b in Lbs:
    a=(math.floor((b/2.2046) * 100 ) )/ 100;
    Wts.append(a)
print(Wts)