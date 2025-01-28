# You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

 

# Example 1:

# Input: n = 10, t = 2

# Output: 10

# Explanation:

# The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.




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

            
            
                

            
