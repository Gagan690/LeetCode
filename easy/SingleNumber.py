class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        status = Counter(nums)
        for key , value in status.items():
            if value == 1:
                return key
