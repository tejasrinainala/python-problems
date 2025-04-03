n = list(map(int, input().split()))

missing = False  # To track if any missing numbers are found

for i in range(len(n) - 1):
    diff = n[i + 1] - n[i]
    
    if diff == 1:
        continue  # Numbers are consecutive, continue checking
    
    elif diff > 1:
        # Print all missing numbers in between
        for num in range(n[i] + 1, n[i + 1]):
            print(num)
            missing = True

# If no missing numbers were found, print message
if not missing:
    print("Sorted and in order!")
