#Het Pathak
#20ce113


#SETS
#a. Write a Python program to add member(s) in a set and clear a set
set1 = set()
set1.add(0)
set1.add(1)
print(set1)
set1.clear()
print(set1)

#b. Write a Python program to remove an item from a set if it is present in the set.
set2 = {0,1,2,3,4,5}
x = 3
if x in set2:
    set2.remove(x)
print(set2)

#c. Write a Python program to create an intersection, Union, difference of sets.
s1 = {1,2,3,4,5}
s2 = {2,4,6,8,0}
inters = s1 & s2
union = s1|s2
dif = s1-s2
print("Intersection :",inters)
print("Union: ",union)
print("Difference: ",dif)

#d. Write a Python program to find maximum and the minimum value in a set.
print("Maximum: :",max(set2))
print("Minimum: ",min(set2))
