class Solution:
    def findMin(self, nums):
        l = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < l:
                l = nums[i]
        return l
