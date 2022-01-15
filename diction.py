#Het Pathak
#20ce113


#DICTIONARIES
#a. Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
x=5
if x in d:
    print('Key is present in the dictionary')
else:
    print('Key is not present in the dictionary')

#b. Write a Python script to merge two Python dictionaries.
d1 = {0:100, 1:200}
d2 = {2:300, 3:400}
d1.update(d2)
print(d1)

#c. Write a Python program to sum all the items in a dictionary.
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
sum =0
for i in dic.values():
    sum+=i
print("Sum: ",sum)

#d. Write a Python script to add a key to a dictionary.
sam_dic = {'a':10,'b':20, 'c':30}
sam_dic.update({'d':40})
print(sam_dic)

#e. Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)