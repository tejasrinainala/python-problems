class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxi = 0
        maxi_sum = 0

        mini = 0
        mini_sum = 0

        for num in nums:
            maxi_sum += num
            maxi = max(maxi, maxi_sum)
            if maxi_sum < 0:
                maxi_sum = 0

            mini_sum += num
            mini = min(mini, mini_sum)
            if mini_sum > 0:
                mini_sum = 0

        return max(abs(maxi), abs(mini))


