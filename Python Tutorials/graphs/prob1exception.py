'''
ATM WIthdrawal System
Scenario
You're sinulating an ATM machine, A user inputs the amount they want to withdraw.
Task:
Raise an error if the amount is more than the account balance.Also handle non-integer input gracefully.
'''
class Insufficientfundserror(Exception):pass
balance=10000
try:
  amount=int(input("Enter the amount"))
  if amount<=0:
    raise ValueError("Withdrawl amount must be grater than than 0")
  if amount> balance:
    raise Insufficientfundserror("Insufficient balance for")
  balance-=amount
  print(f"Withdrawl successful! Remainid balance: {balance}")
except ValueError as ve:
  print("Invalid input")