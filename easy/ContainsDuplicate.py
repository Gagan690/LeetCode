class Solution:
    def containsDuplicate(self, nums):
        s = set(nums)
        if len(s) != len(nums):
            return True
        else:
            return False
