'''
num=100
print("Program Exceution Begins")
print(num)
try:
  print(num/0)
except ZeroDivisionError:
  print("Dividing with Zero Gives Infinite Values")
print("Program Exceution Ends")
'''




'''
num=100
print("Program Exceution Begins")
print(num)
try:
    print(num/10)
finally:
     print("Dividing with Zero Gives Infinite Values")
print("Program Exceution Ends")

'''


a=10
b=5
try:
  d=a/b
  print(d)
  print('Inside Try')

except ZeroDivisionError:
  print('Divsion by Zero Not allowed')

else:
  print('Inside Else')

print("Rest of The code")