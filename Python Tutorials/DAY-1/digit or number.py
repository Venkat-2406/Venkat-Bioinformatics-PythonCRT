a=int(input("Enter the number"))
if a>=-9 and a<=9:
  print(f"{a} is digit")
else:
  print(f"{a} is number")
#ternary operator
res="digit" if a>=-9 and a<=9 else "number"
print(f"{a} is {res}")