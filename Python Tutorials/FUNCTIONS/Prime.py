#Prime numbers using functions
def prime(num):
  count=0
  for i in range(1,num+1):
    if num%2==0:
      count+=1
  if count==2:
      print(f"{num} is prime")
  else:
      print(f"{num} is not prime")
prime(100)
prime(5)