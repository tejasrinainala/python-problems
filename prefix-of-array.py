class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        phr=['']
        for i in range(len(words)):
            if i==0:
                phr.append(words[i])
            else:
                phr.append(phr[-1]+words[i])
        if s in phr:
            return True
        else:
            return False
            
            
        
