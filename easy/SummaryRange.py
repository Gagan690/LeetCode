class Solution:
    def summaryRanges(self, nums):
        i = 0
        n = len(nums)
        result = []

        while i < n:
            start = nums[i]
            j = i

            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1

            end = nums[j]

            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))
            i = j + 1

        return result
