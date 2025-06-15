n=int(input("Enter the number of elements :"))
list=[]
for i in range(n):
    temp=input("Enter the elements :")
    list.append(temp)
print(f"Before swapping the list is {list}")
if len(list)>2:
    list[0],list[-1]=list[-1],list[0]
print(f"After swapping the first and last element list is {list}")
