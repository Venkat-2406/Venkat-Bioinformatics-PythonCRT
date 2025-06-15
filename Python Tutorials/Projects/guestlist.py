#program to find the quest list
#Add confirmed quest
#remove the quest who cancel
#check if friend is on the list or not
#print the final guest list
guest_list=[]
while(True):
  print('**********menu************')
  print("1.add the guest")
  print("2.remove the quest who cancel")
  print("3.check if friend is on the list or not")
  print("4.print the final guest list")
  print("------------------------------------------")
  choice=int(input("Enter the choice"))
  if choice>=1 and choice<=5:
    if choice==1:
      gname=input("enter the gname:")
      guest_list.append(gname)
      print(f'{guest_list} is added into list')
    elif choice==2:
      cguest=input("enter the name of cguest:")
      if cguest in guest_list:
        guest_list.remove(cguest)
        print(f"{cguest} is removed from guestlist")
      else:
        print(f'{cguest} is not in guest list')
    elif choice==3:
      chguest=input("Enter the guest  name :")
      if chguest in guest_list:
        print(f'{chguest} is attending the party')
      else:
        print(f'{chguest}is not attending the party')
    elif choice==4:
      if len(guest_list)==0:
        print(f'{guest_list} is empty')
      else:
        guest_list.sort()
        print("hurray here i0s final quest list")
        print(guest_list)
    else:
      print("enjoy your party")
      break
  else:
    print("Invalid")

