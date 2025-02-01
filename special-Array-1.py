# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

# Input: nums = [2,1,4]

# Output: true

# Explanation:

# There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.




class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l=0
        r=1
        c=0
        if len(nums)==1:
            return True
        else:
            for i in range(len(nums)-1):
                if nums[l]%2==0 and nums[r]%2!=0:
                    c+=1
                elif nums[l]%2!=0 and nums[r]%2==0:
                    c+=1
                l+=1
                r+=1
        if c==len(nums)-1:
            return True
        else:
            return False



        
