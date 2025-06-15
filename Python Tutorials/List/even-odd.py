numbers=[]
even=[]
odd=[]
n=int(input("ENter the size of numbers :"))
for i in range(n):
  temp=int(input("Enter the numbers : "))
  numbers.append(temp)
for i in numbers:
    if i%2==0:
      even.append(i)
    else:
      odd.append(i)
print(even)
print(odd)
