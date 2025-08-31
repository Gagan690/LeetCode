class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        n = len(nums)
        total = []
        for i in range(0,n,2):
            total.append(min(nums[i],nums[i+1]))
        return sum(total)
