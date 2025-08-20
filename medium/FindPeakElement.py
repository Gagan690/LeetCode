class Solution:
    def findPeakElement(self, nums):
        first_num = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[first_num]:
                first_num = i

        return first_num
