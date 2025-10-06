class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        status = Counter(nums)
        for key , values in status.items():
            if values == 1:
                return key
