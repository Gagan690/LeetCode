from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = Counter(nums)
        return majority.most_common(1)[0][0]
