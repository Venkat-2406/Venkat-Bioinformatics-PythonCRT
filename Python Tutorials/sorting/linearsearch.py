arr=[5,6,2,3,4,1,0,7,8,9]
def Linearsearch(key,arr,len):
  for i in range(len):
    if arr[i]==key:
      return i
  return None
res=Linearsearch(1,arr,10)
if res is None:
  print("Element not found")
else:
  print(f"Element found at {res} index")




'''
def LinearSearch(key,arr,len):
    count=0
    for i in range(len):
        count+=1
        print(f"{count}Iteration")
        if arr[i]==key:
            print(f"Element found at index {i}")
            break
    else:
        print("Element not found.")
res=LinearSearch(9,[5,6,2,3,4,1,0,7,8,9],10)
'''