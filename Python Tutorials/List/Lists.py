#user input list

n=int(input())
b=[]
for i in range(n):
    temp=input()
    b.append(temp)
print(b) 

n=int(input())
b=[]
for i in range(n):
    temp=input()
    b.append(temp)
print(b) 
print(len(b))
print(max(b))
print(min(b))
print(sorted(b))

#reversind without reversing a string
n=int(input())
b=[]
for i in range(n):
    temp=input()
    b.append(temp)
print(b)
print(b[-1::-1])

#sorting without using sort
n=int(input())
b=[]
for i in range(n):
    temp=input()
    b.append(temp)
print(b)
for i in range(0,len(b)):
    for j in range(i+1,len(b)):
        if b[i]>=b[j]:
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
print(b)

