scores=[55,90,70,60,80]
print(f"Original Array :{scores}")
for i in range(len(scores)):
  flag=False
  for j in range(len(scores)-1):
    if (scores[j]>scores[j+1]):
      temp=scores[j]
      scores[j],scores[j+1]=scores[j+1],scores[j]
      print(scores)
      Flag=True
    if flag==False:
      break
print("sorted array",scores)






