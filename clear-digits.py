# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

 

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isalpha():
                stack.append(char)
            elif char.isdigit() and stack:
                stack.pop()  
        return ''.join(stack)


        
