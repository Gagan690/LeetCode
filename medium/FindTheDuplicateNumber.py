class Solution:
    def findDuplicate(self, nums):
        nums = sorted(nums)
        nums_len = len(nums)
        for i in range(nums_len+1):
            if nums[i] == nums[i+1]:
                return nums[i]
