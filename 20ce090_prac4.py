n = int(input("Enter total elements: "))
li=[]

for i in range(0,n):
    li_ele = int(input())
    li.append(li_ele)

length = len(li)

for i in range(0, length-1):
    for j in range(length-1):
        if li[j]<li[j+1]:
            li[j], li[j + 1] = li[j + 1], li[j]


res = li.count(li[0]) == len(li)

if li[0]==li[1]:
    runner_up=li[2]
else:
    runner_up = li[1]


if not res:
    print(f"Runner's up: {runner_up}")
else:
    print("All scores are equal")