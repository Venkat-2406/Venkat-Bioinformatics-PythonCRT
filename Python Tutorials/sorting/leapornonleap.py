n=int(input("Enter the year"))
if n%4==0 and n%100!=0:
  print("leap year")
else:
  print("Non-leap year")