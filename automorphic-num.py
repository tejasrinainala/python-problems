num = int(input())
numsq = num * num

# Convert both to strings and check if numsq ends with num
if str(numsq).endswith(str(num)):
    print("Yes")
else:
    print("No")


