# 1. In a bustling chocolate factory, workers are busy packing chocolates into packets. Each packet is represented by an array of integers, where `0` signifies an empty packet. The factory manager has tasked you with finding all the empty packets and pushing them to the end of the array.
# Example

# Input
# N = 8
# arr = [4, 5, 0, 1, 9, 0, 5, 0]
# Output
# 4 5 1 9 5 0 0 0

def move_zeroes(arr):
    count = 0  # Count of non-zero elements
    for num in arr:
        if num != 0:
            arr[count] = num
            count += 1
            
    while count < len(arr):
        arr[count] = 0
        count += 1

arr = [4, 5, 0, 1, 9, 0, 5, 0]
move_zeroes(arr)
print(arr)
