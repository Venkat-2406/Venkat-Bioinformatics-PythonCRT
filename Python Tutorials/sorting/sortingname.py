arr=['Amy','Scott','Bill','Xmen']
length=len(arr)
print(f"Original Array :{arr}")
for i in range(length-1):
  for j in range(length-i-1):
    if (arr[j]>arr[j+1]):
      temp=arr[j]
      arr[j]=arr[j+1]
      arr[j+1]=temp
print("sorted array",arr)

4,2,2,8,4,6
2,4,6,8
