class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        l = 0
        total = 0
        result = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                result = min(result, r - l + 1)
                total -= nums[l]
                l += 1

        return result if result != float("inf") else 0

print(Solution().minSubArrayLen(11,[1,2,3,4,5]))
