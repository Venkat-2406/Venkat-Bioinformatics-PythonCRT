songs=[]
n=int(input("ENter the size of playlist :"))
for i in range(n):
  temp=input("Enter the list of songs : ")
  songs.append(temp)
print(songs)
print(songs[-1::-1])




