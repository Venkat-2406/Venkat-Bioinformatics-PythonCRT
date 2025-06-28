arr=[4,2,2,8,4,6]
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
new_list=[]
for i in arr:
  if i not in new_list:
    new_list.append(i)
print(new_list)