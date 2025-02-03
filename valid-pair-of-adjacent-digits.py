# Input: s = "2523533"

# Output: "23"

# Explanation:

# Digit '2' appears 2 times and digit '3' appears 3 times. Each digit in the pair "23" appears in s exactly as many times as its numeric value. Hence, the output is "23".



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
            
