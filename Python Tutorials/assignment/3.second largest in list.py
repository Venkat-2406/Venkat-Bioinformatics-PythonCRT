# 3. Find the Second Largest Number in a List
n=int(input("Enter the number of elements :"))
list=[]
for i in range(n):
    temp=input("Enter the elements :")
    list.append(temp)
m=sorted(list)
print(m[-2])
