class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        
        for i in range(len(strs[0])):
            char = strs[0][i]

            
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        
        return strs[0]
