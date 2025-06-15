#write a python program 
# to display a menu of food items (LIST)
#create a tuple of prices with respect to food items
#read from user to order the food including the quantity 
#             ----if exists in menu
#             ----if not exists---not available
# While billing,read phone number,feedback,read tip amount
#add 18% GST to bill and print the bill if bill>0

food_items=[]
while(True):
  print('**********menu************')
  print("1.Display the food item list")
  print("2.Prices with respect to food items")
  print("3.Order the food")
  print("4.Billing")
  print("------------------------------------------")
  choice=int(input("Enter the choice"))
  if choice==1:
    starters=['chicken kawab','lollipop','dragon chicken']
    print(f"Starters available are {starters}")
    course=['biryani','mutton biryani','fish biryani']
    print(f"main_course available are {course}")
    drinks=['coke','7up','Bindu']
    print(f"Available drinks are {drinks}")
  elif choice==2:
    n=int(input("Enter no of items that u want to order "))
    i=1
    starters=['chicken kawab','lollipop','dragon chicken','biryani','mutton biryani','fish biryani','coke','7up','bindu']
    price=('250','350','400','150','200','300','10','15','20')
    while(i<=n):
      word=input("Enter the food item")
      index=starters.index(word)
      print(f"{word}-{price[index]}")
      i+=1
  elif choice==3:
    order=[]
    for item in food_items:
     


