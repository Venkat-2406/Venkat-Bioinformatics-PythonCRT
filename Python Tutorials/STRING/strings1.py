#Program to read a string from user(including spaces) and print the string the by trimming the spaces
#Python program to read a string a input
#1.	Print the string as list of individual char
#2.	Find the length of string
#3.	Find the min element of converting str into list.	
#5.	Find the no.of spaces present in the string without using functions and methods

#print the string the by trimming the spaces
a=input("Enter the string :")
b=a.replace(" ","")
print(b)
#1.	Print the string as list of individual char
for x in a:
  print(x,end=' ')
print()
#2.	Find the length of string
print(len(a))
#3.	Find the min element of converting str into list.	
c=list(a)
print(min(c))
#5.	Find the no.of spaces present in the string without using functions and methods
count=0
i=0
while i<len(a):
  if a[i]==' ':
    count+=1
  i=i+1
print(count)
