n = int(input("Enter the number of dates: "))
arr = []

for i in range(n):
    date = input(f"Enter date {i+1} (dd-mm-yyyy): ")
    arr.append(date)

for i in range(n - 1):
    for j in range(n - i - 1):
        d1, m1, y1 = arr[j].split("-")
        d2, m2, y2 = arr[j + 1].split("-")
        
        d1, m1, y1 = int(d1), int(m1), int(y1)
        d2, m2, y2 = int(d2), int(m2), int(y2)

        if y1 > y2 or (y1 == y2 and m1 > m2) or (y1 == y2 and m1 == m2 and d1 > d2):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted dates from earliest to latest:")
for date in arr:
    print(date)
