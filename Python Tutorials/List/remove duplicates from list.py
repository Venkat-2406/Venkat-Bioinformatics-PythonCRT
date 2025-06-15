list=[12,24,67,98,98,76,45,3,25,16]
b=[]
for item in list:
  if item not in b:
    b.append(item)
print(b)