# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.





class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map={')':'(','}':'{',']':'['}
        for i in s:
            if i in map.values():
                stack.append(i)
            elif i in map:
                if stack and stack[-1]==map[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
        
