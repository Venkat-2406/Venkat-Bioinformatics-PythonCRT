arr=[10,50,60,20,40,30]
length=len(arr)
print(f"Original Array :{arr}")
for i in range(length-1):
  for j in range(length-i-1):
    if (arr[j]>arr[j+1]):
      temp=arr[j]
      arr[j]=arr[j+1]
      arr[j+1]=temp
print("sorted array",arr)
print(length)









arr=[25,20,15,10,5]
print(f"Original Array :{arr}")
count=0
for i in range(len(arr)):
  flag=False
  for j in range(len(arr)-1):
    if (arr[j]>arr[j+1]):
      temp=arr[j]
      arr[j],arr[j+1]=arr[j+1],arr[j]
      print(arr)
      Flag=True
    if Flag==False:
      break
print("sorted array",arr)






















