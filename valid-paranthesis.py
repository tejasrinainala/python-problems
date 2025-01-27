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
        
