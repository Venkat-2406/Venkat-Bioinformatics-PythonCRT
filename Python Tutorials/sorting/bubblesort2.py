arr=[25,20,15,10,5]
print(f"Original Array :{arr}")
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