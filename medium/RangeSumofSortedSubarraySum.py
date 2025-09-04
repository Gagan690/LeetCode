import heapq

class Solution:
    def rangeSum(self, nums, n: int, left: int, right: int) -> int:
        min_heap = []
        for i in range(n):
            heapq.heappush(min_heap, (nums[i], i))

        total_sum = 0
        for k in range(right):
            current_sum, end_index = heapq.heappop(min_heap)
            if k >= left - 1:
                total_sum += current_sum
            if end_index + 1 < n:
                heapq.heappush(min_heap, (current_sum + nums[end_index + 1], end_index + 1))

        return total_sum % (10**9 + 7)
