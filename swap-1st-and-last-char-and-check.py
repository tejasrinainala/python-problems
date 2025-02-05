class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l=[]
        if s1==s2:
            return True
        else:
            l=list(s2)
            l[0],l[len(l)-1]=l[len(l)-1],l[0]
            s2="".join(l)
            if s1==s2:
                return True
            else:
                l=list(s1)
                l[0],l[len(l)-1]=l[len(l)-1],l[0]
                s1="".join(l)
                if s1==s2:
                    return True
                else:
                    return False
        
