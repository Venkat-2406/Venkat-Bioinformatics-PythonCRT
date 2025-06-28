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
finally:
  print('INside Finally')
print("Rest of The code")