class Solution:
    def findValidPair(self, s: str) -> str:
        l=0
        r=1
        n=""
        for i in range(len(s)-1):
            if (s.count(s[l])==int(s[l]) and s.count(s[r])==int(s[r])) and s[l]!=s[r]:
                n+=s[l]
                n+=s[r]
                return n
            else:
                l+=1
                r+=1
        return n
            
