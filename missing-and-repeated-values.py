import numpy as np

arr = np.array([[9, 1, 7], [8, 9, 2], [3, 4, 6]])
arr = arr.flatten()
sor = sorted(arr)  # Sort the array

repeated = -1
missing = -1
num_set = set()

# Find the repeated number
for num in sor:
    if num in num_set:
        repeated = num
    num_set.add(num)

# Find the missing number
for i in range(len(sor) - 1):
    if sor[i + 1] - sor[i] > 1:  # If there's a gap
        missing = sor[i] + 1
        break

print([repeated, missing])  # Output: [9, 5]
