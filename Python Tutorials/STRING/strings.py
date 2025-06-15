#string declarations.....
str1='Good morning'
print(type(str1))

str2='I am the "great" person'
print(str2)
print(type(str2))

str3="""I am the "great" person"""
print(str3)
print(type(str3))

str4='''I am the "great" person'''
print(str4)
print(type(str4))

a=10
b='10'
print(id(a))
print(id(b))
print(a is b)

str='python'
print(f"Length of {str} is {len(str)}")
#accesing without index
for i in str:
  print(i,end=' ')
print()
  #accesing through len
for i in range(len(str)):
 print(str[i],end=' ')

str4="Students"
str4=[4]='i'
for c in str4:
  print(c)


str5='python programming'
print(str5[1:6])
print(str5[0])
print(str5[7:11])
print(str5[10:14])
print(str5[7:10])
print(str5[2:6])
print(str5[::-1])
print(str5[-9::])
print(str5[-1:-8:-1])
print(str5[-4:-8:-1])

#concatenation of String
a='Hello'
b='world'
c=a+b
print(c)

# Removing the space in stringg
input=input("Enter the string :")
s=input.split()
print(s)

#join methods
str1="H"
str2="hi"
s=str1+str2
print(s)


#Splitting the string
sentence="We are learning python"
list=sentence.split()
print(list)

#String methods
str='Python Program'
print(str[::-1])
print(str.lower())
print(str.upper())
print(str.swapcase())


str='P','y','t','h','o','n'
c="".join(str)
print(c)

#Program to read the mail id as input from the user and print the user name and organization name
#(name@orgname.com) output:name,orgname
mail=input("Enter the mail id :")
list=mail.split("@")
print(f"User name :{list[0]}")
org=list[1]
list=org.split('.')
print(f"org name :{list[0]}")

mail=input("Enter the mail id :")
n=mail.removesuffix(".com")
print(n)

#methods in string
str='python program'
print(str.capitalize())
print(str.title())
print(str.casefold())
print(str.startswith("p"))
print(str.find('o'))
print("Hi".center(15,'*'))

#problem on counting the no of uppercase and lower case
str=input("Enter the string :")
uppercase=0
lowercase=0
numeric=0
splchar=0
for ch in str:
  if ch.isupper():
    uppercase+=1
  elif ch.islower():
    lowercase+=1
  elif ch.isdigit():
    numeric+=1
  else:
    splchar+=1
print(uppercase)
print(lowercase)
print(numeric)
print(splchar)


#Program to take a name as user including the prefix mr/ms.print the gender classification of name on basis of prefix
a=input("Enter the size of  string :")
if a.startswith("mr"):
  print("male")
else:
  print("female")



#Program to read a string from the user and print the count of
#1.uppercase vowels
#2.lowercase vowels
#3.uppercase consonants
#4.lowercase consonants
str=input("Enter the string :")
uvowels=0 
lvowels=0
uconso=0
lconso=0
for ch in str:
  if ch.isalpha() and ch.isupper():
    if ch in 'AEIOU':
      uvowels+=1
    else:
      uconso+=1
  if ch.isalpha() and ch.islower():
    if ch in 'aeiou':
      lvowels+=1
    else:
      lconso+=1  
print(uconso)
print(lconso)
print(uvowels)
print(lvowels)

#Program to print the uppercase alphabets a to z including asc2 values
for i in range(1,27):
  print(chr(i+64),"----->",i+64)
print("----------------")
for i in range(1,27):
  print(chr(i+96),"----->",i+96)


a=input(" Enter the char")
print(ord(a))


#Program to read a string from the user and replace all vowels with zero
a=input("Enter the string :")
b=a.lower()
c=a
for ch in 'aeiou':
  c=c.replace(ch,"0")
print(c)

