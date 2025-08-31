class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sort = sorted(nums)
        result = []
        for num in nums:
            result.append(sort.index(num))
        return result
