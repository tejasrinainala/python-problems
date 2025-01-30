class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0
        nums = nums1 + nums2
        merge_arr = sorted(nums)
        if len(merge_arr) % 2 != 0:
            median = merge_arr[len(merge_arr) // 2 + 1 // 2]
        else:
            median = (
                merge_arr[(len(merge_arr) // 2) - 1]
                + merge_arr[(len(merge_arr) // 2) - 1 + 1]
            ) / 2
        return median
