list1 = []
revlist = []

# Input values until an empty line is entered
while True:
    user_input = input("Enter a number (or press Enter to stop): ")
    if user_input == "":
        break
    list1.append(int(user_input))

# Compute squares and store them in revlist
for num in list1:
    revlist.append(num * num)

# Reverse revlist
revlist.reverse()

print("Reversed list of squares:", revlist)


# output:
# Enter a number (or press Enter to stop): 2
# Enter a number (or press Enter to stop): 3
# Enter a number (or press Enter to stop): 4
# Enter a number (or press Enter to stop): 5
# Enter a number (or press Enter to stop): 
# Reversed list of squares: [25, 16, 9, 4]
