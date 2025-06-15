n=int(input())
b=[]
c=[]
for i in range(n):
  temp=int(input("Enter the numbers"))
  b.append(temp)
for i in b:
  if (i%5==0):
    c.append(i)
print(c)
