class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            n1=i-k
            n2=i+k
            if (n1>=0 and nums[i]<=nums[n1]) or (n2<len(nums) and nums[i]<=nums[n2]):
                continue
            c+=nums[i]
        return c©leetcode
