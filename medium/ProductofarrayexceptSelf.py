class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        preflix = 1
        for i in range(n):
            result[i] *= preflix
            preflix *= nums[i]

        suflix = 1
        for i in range(n-1,-1,-1):
            result[i] *= suflix
            suflix *= nums[i]

        return result
