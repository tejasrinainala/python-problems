# Jack loves Sundays. He wants to know how many Sundays will occur in a month starting on any given day. Given the starting day and the total number of days in the month, your task is to find out the number of Sundays.
# Input

# A string indicating the first day of the month (e.g., "mon") and an integer representing the total number of days in that month.
# Output

# The number of Sundays in that month.



user = input().lower()      # starting day
nd = int(input())           # number of days in the month
c = 0
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

start_index = days.index(user)  # get the starting day index

for i in range(nd+1):  # loop over each day of the month
    # find the weekday for the current day
    day_index = (start_index + i) % 7
    if days[day_index] == 'sunday':
        c += 1

print(c)



# output:
# monday
# 13
# 2
