n=int(input("Enter the number of elements :"))
list=[]
for i in range(n):
    temp=int(input("Enter the elements :"))
    list.append(temp)
if len(list)==0:
    print("The list is Empty")
else:
  avg=sum(list)/len(list)
print(f"The average of numbers is {avg}")
