class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        pro=1
        k=n
        r=0
        for i in range(10):
            k=n
            pro=1
            while(k>0):
                r=k%10
                pro=pro*r
                k=k//10
            if pro%t==0:
                return n
            else:
                n=n+1

            
            
                

            
