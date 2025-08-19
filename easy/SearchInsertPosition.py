class Solution:
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0

        nums.append(target)
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
