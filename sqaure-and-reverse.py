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
