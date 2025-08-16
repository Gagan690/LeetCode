class Solution:
    def missingNumber(self, nums):
        nums = sorted(nums)
        nums.append(0)
        nums_len = len(nums)
        if nums[0] != 0:
            return 0
        for i in range(nums_len+1):
            if nums[i] + 1 != nums[i+1]:
                return nums[i] + 1
            else:
                continue
