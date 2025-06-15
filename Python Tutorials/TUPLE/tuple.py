#tuple packing
tuple=10,20,30,40,50,60,70,80,90,100
print(tuple)
print(type(tuple))
#tuple unpacking
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10=tuple
print(n1,type(n1))
print(n2,type(n2))

#adding and Concatenation
a=[10,20,30]
b=[1,2,3]
res=a+b
print(res)

#repetition for list
b=[1,2,3]
res=b*3
print(res)

#repetition for tuple
b=(1,2,3)
res=b*3
print(res)

#nested tuple
tuple=(('a','b','c'),('A','B','C'))
print(tuple)
for i in tuple:
  print(i,type(tuple))

#functions
tuple=(10,20,60,55,44,11)
print(tuple)
print(max(tuple))
print(min(tuple))


#Program to create a tuple of programming languages being len as 15 and find the max element and min and print the sorted tuple and the reserved tuple
tuple=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(len(tuple))
print(tuple[-1::-1])
print()