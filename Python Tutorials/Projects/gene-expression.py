
n=int(input("Enter the size of data :"))
list=[]
list1=[]
for i in range(n):
  temp=float(input("Enter the value :"))
  list.append(temp)
for i in list:
  if i<5:
    list1.append("Underexpressed")
  elif i>=5 and i<=15:
    list1.append("Normal")
  else:
    list1.append("Overexpressed")
print(list1)