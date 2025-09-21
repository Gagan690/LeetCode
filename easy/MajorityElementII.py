class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        result = []
        for elements, count in counts.items():
            if count > n // 3:
                result.append(elements)
        return result
