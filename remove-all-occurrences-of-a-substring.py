class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        arr=[]
        index=0
        if part not in s:
            return s
        else:
            while s.find(part) != -1:
                index = s.find(part)  
                s = s[:index] + s[index + len(part):]

        return s

        
