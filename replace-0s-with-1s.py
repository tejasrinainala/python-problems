#replace all 0s with 1s


# Take input as a string to preserve leading zeros
x = input().strip()

# Replace all '0's with '1's if the number contains '0'
if '0' in x:
    x = x.replace('0', '1')

# Print the result as an integer
print(int(x))
