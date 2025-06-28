'''
syntax : name=[expression for item in iterable object if _ statment]
There can be 0 or 1 if statments in condition
'''


num=[]
for i in range(1,11):
  num.append(i)
print(num)

#using list comprehension
new=[i for i in range(1,11)]
print(new)


'''
program to print even numbers from one to n using list comprehension
'''
n=int(input())
new=[i for i in range(1,n) if i%2==0]
print(new)