import statistics
Ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
Ages.sort()
print("After Sorting the list: ", Ages)

#Add the min age and the max age again to the list
Min = min(Ages)
Max = max(Ages)
print("Minimum value in list : " , Min ,"\n"  "Maximum value in list : " , Max)
Ages.append(Min) #Appending
Ages.append(Max)
print("After appending the list:", Ages)

#Find the median age (one middle item or two middle items divided by two)
Med = statistics.median(Ages)
print("Median of the list:", Med)

#Find the average age (sum of all items divided by their number)
Sum = sum(Ages);
Length = len(Ages);
Average = Sum/Length;
print("Average of the list : ", Average);

#Range
Range = Max - Min;
print("Range of the list :", Range);







