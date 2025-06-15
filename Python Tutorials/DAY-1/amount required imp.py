# input as amount and get a required amount in notes in indian currency
a=int(input("Enter the amount"))
print("2000---",a//2000)
a=a%2000
print("500---",a//500)
a=a%500
print("200---",a//200)
a=a%200
print("100---",a//100)
a=a%100
print("50---",a//50)
a=a%50
print("20---",a//20)
a=a%20
print("10---",a//10)
a=a%10
print("2---",a//2)
a=a%2
print("1---",a//1)