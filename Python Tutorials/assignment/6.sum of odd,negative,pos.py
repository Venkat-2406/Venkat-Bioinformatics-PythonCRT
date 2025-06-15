#6.Print Sum of Negative Numbers, Positive Even Numbers, and Positive Odd Numbers in a List
#Write a program that takes a list of integers and calculates:

#* The sum of all negative numbers
#* The sum of all positive even numbers
#* The sum of all positive odd numbers
 # Display each sum clearly.


n=int(input("Enter the number of elements :"))
list=[]
neg_list=[]
pos_num=[]
odd_num=[]
for i in range(n):
    temp=int(input("Enter the elements :"))
    list.append(temp)
for item in list:
    if item<0:
        neg_list.append(item)
    elif item>0 and item%2==0:
        pos_num.append(item)
    else:
        odd_num.append(item)
print(f"The sum of negative numbers is {sum(neg_list)}")
print(f"The sum of positive even numbers is {sum(pos_num)}")
print(f"The sum of all positive odd numbers is {sum(odd_num)}")
