class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        total_nums = nums1 + nums2
        total = 0
        for i in total_nums:
            total += i
        return total/len(total_nums)
