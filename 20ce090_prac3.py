size=int(input())
arr=[ ]
for i in range(size):
    element=int(input())
    arr.append(element)
unique = [i for i in arr if arr.count(i) == 1]
room_no = str(unique)

print(arr)
print("Captain's room: ",room_no)
