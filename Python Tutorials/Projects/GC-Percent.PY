#Count (G + C)/Count (A + T + G + C) * 100% Calculate the gc content
seq=input("Enter the size of data :")
count=0
count1=0
for i in seq:
  if i=='C' or i=='G':
    count+=1
for i in seq:
  if i=='A' or i=='G' or i=='T' or i=='C':
    count1+=1
gc=count/count1*100
print(gc)
if gc>60: 
  print("High GC")
elif gc>=40 and gc<=60:
  print("Moderate")
else:
  print("LOw GC")






























