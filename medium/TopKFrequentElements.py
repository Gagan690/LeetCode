import heapq
class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)

        min_heap = []

        for key , value in count.items():
            heapq.heappush(min_heap , (value , key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        result = [item[1] for item in min_heap]
        return result
