import random
import string
name = str(input("Enter a name : "))
city = str(input("Where do you live ? "))
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['1','2','3','4','5','6','7','8','9','0']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
                      '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?', '`', '~']
pre_name = name[3]
pre_city = city[2]
raw_password = pre_name+pre_city

password = raw_password[:6]
has_upper = False
has_lower = False
has_digit = False
has_special = False

# Check what kind of characters are already in the password
for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if char in string.punctuation:
        has_special = True

# If the password doesn't meet the requirements, add the missing characters
if not has_upper:
    password += uppercase_letters[random.randint(0,len(uppercase_letters)-1)]
if not has_lower:
    password += lowercase_letters[random.randint(0,len(lowercase_letters)-1)]
if not has_digit:
    password += digits[random.randint(0,len(digits)-1)]
if not has_special:
    password += special_characters[random.randint(0,len(special_characters)-1)]

# Step 6: If the password is longer than 6 characters, trim it to 6
while len(password) > 6:
    password = password[:6]

# Print the generated password
print("Generated password:", password)

