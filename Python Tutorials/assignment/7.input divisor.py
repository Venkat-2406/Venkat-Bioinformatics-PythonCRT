#7. Divide All Elements of a List by a Number
#Write a program that accepts a list of numbers and a divisor. Divide each element of the list by the divisor and return a new list with the results. Ensure the divisor is not zero.
n=int(input("Enter the number of elements :"))
list=[]
quo_list=[]
for i in range(n):
    temp=int(input("Enter the elements :"))
    list.append(temp)
m=int(input("Enter the Divsior :"))
if m==0:
    print("Divisor should not be zero ")
else:
    for item in list:
        quo=item//m
        quo_list.append(quo)
print(quo_list)
