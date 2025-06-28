#program to month number as input from user print no of respective days of month
month=int(input())
if month in [4,6,9,11]:
  print("30 days")
elif month in [1,3,5,7,8,10,12]:
  print("31 days")
else:
  print("28 or 29 days")

