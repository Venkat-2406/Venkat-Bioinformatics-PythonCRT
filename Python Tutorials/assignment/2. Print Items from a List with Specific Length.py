#2. Print Items from a List with Specific Length
n=int(input("Enter the number of elements :"))
list=[]
count=0
for i in range(n):
    temp=input("Enter the elements :")
    list.append(temp)
m=int(input("Enter the Length to separate strings from list :"))
for item in list:
    if len(item)==m:
        print(item)