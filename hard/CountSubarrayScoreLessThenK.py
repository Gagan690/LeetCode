class Solution:
    def countSubarray(self, nums, k):
        count = 0
        n = len(nums)
        left = 0
        current_sum = 0

        for right in range(n):
            current_sum += nums[right]
            while current_sum * (right - left + 1) >= k and left <= right:
                current_sum -= nums[left]
                left += 1
            count += (right - left + 1)
        return count

# Example usage:
print(Solution().countSubarray([2,1,4,3,5], 10))
