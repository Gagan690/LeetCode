class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n

        max_len = 0
        end_index = -1

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                end_index = i

        result = []
        current_index = end_index
        while current_index != -1:
            result.append(nums[current_index])
            current_index = prev[current_index]

        return result[::-1]
