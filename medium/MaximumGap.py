class Solution:
    def maximumGap(self, nums):
        if not nums or len(nums) <= 1:
            return 0

        num = sorted(nums)
        longest = num[1] - num[0]
        for i in range(len(num)-1):
            diff = num[i+1] - num[i]
            if diff > longest:
                longest = diff
        return longest
