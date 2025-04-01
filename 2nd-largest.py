a = list(map(int, input().split()))  # Take space-separated integers as input

a = list(set(a))  # Remove duplicates
a.sort(reverse=True)  # Sort in descending order

if len(a) < 2:
    print("No second largest element")
else:
    print(a[1])  # Second largest element
