#program to create a customer service by adding customer into the queue once served he has to be removed from the queue
from collections import deque

# Initialize queue
customer_queue = deque()

while True:
    print("\n--- Customer Service Menu ---")
    print("1. Add Customer to Queue")
    print("2. Serve Customer")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter customer name: ")
        customer_queue.append(name)
        print(f"{name} has been added to the queue.")

    elif choice == '2':
        if not customer_queue:
            print("No customers to serve.")
        else:
            served = customer_queue.popleft()
            print(f"{served} has been served and removed from the queue.")
    else:
        print("Invalid choice. Please select 1 to 2.")


