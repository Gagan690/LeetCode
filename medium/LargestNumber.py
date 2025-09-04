from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        nums_str = [str(num) for num in nums]

        def compare(s1, s2):
            if s1 + s2 > s2 + s1:
                return -1
            elif s1 + s2 < s2 + s1:
                return 1
            else:
                return 0

        nums_str.sort(key=cmp_to_key(compare))

        result = "".join(nums_str)

        if result[0] == '0':
            return '0'
        else:
            return result
