a=int(input("Enter the value"))
temp=a
count=0
while a!=0 and a<0:
  a=a//10
  count+=1
print(f"{temp} has {count} digits")