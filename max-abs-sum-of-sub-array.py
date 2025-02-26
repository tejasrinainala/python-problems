# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
 

# Example 1:

# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.


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


