# Write a Python program to create a Dictionary with Every character in the string as a key and its frequency as the value for the key
word = input("Enter a word: ")
frequency_dict = {}

for char in word:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1

print(frequency_dict)
