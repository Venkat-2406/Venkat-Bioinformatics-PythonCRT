def mutiplication(num):                                         # multiplications of n tables
   i=1
   for i in range(1,num+1):
      print(f"mutliplication table of {i}")
      for j in range(1,11):
         print(f"{i} * {j} = {i*j}")
mutiplication(10)
