
num=[10,20,30,40,50,60,70,80]
print(num)
print(type(num))
print("Numbers from positive indexing")
print(num[0])
print(num[1])
print(num[2])
print(num[3])
print("NUmbers from negative indexing")
print(num[-8])
print(num[-7])
print(num[-6])
print(num[-5]) 


# accesing the elements through loops
num=[10,20,30,40,50,60,70,80,90]
for i in range(len(num)):
  print(num[i])  


num=[10,20,30,40,50,60,70,80,90]
i=0
while (i<len(num)):
  print(num[i])
  i+=1


  #Taking multiple inputs from the user
size=int(input("Enter the size of list"))
n=[]
for i in range(size):
    temp=input("Enter the n")
    n.append(temp)
print(n)


#delete an element and list in list
color=['yellow','red','blue','pink']
print(color)
del color[2]
print(color)
del color
print(color)
 
#Using in built functions
n=int(input())
num=[]
for i in range(n):
    temp=int(input(f"Enter the element at {i} index:"))
    num.append(temp)
print(f"Given list is {num}")
print("Maximum",max(num))
print("Minimum",min(num))
print("Sum is",sum(num))
print(sorted(num)) 


#bulit in functions append...insert..pop..remove...reverse
n=['1','2','3','4']
print(n)
n.append('5')
print(n)
n.insert(0,10)
print(n)
n.pop()
print(n)
n.remove('4')
print(n)
o=n.index('2')
print(o)
n.reverse()
print(n)
n=['1','2','3','4']
print(n[0::])
print(n[1::2])


#extend function
a=['apple','bannana','pineapple','grape']
print(a)
b=['car','bus','aeroplane','bike']
print(b)
a.extend(b)
print(a)


a=['SOL','NO SQL','DJANGO']
print(a)
b=['c','java','python','java script']
a.extend(b)
print(a)
print(b.count('java'))       # count function
