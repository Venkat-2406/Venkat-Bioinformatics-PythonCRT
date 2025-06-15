#Count the Number of Null Elements in a List
n=int(input("Enter the number of elements :"))
list=[]
count=0
for i in range(n):
    temp=input("Enter the elements :")
    list.append(temp)
for item in list:
    if item=="":
      count+=1
print(count)
