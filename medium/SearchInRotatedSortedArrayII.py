class Solution:
    def search(self, nums, target):
        nums = set(sorted(nums))
        for i in nums:
            if i == target:
                return True
        return False
