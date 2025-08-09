from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):

        
        """First Method """
        # for i in range(indexDiff):
        #     for j in range(i+1,min(i+indexDiff+1, len(nums))):
        #         if abs(nums[i] - nums[j]) <= valueDiff:
        #             return True
        # return False

        # for i in range(len(nums)):
        #     for j in range(i + 1, min(i + indexDiff + 1, len(nums))):
        #         if abs(nums[i] - nums[j]) <= valueDiff:
        #             return True
        # return False


        """Second Method"""
        window = SortedList()
        for i in range(len(nums)):
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])

            idx = window.bisect_left(nums[i] - valueDiff)
            if idx < len(window) and window[idx] <= nums[i] + valueDiff:
                return True
            window.add(nums[i])

        return False


print(Solution().containsNearbyAlmostDuplicate([1,2,3,1],3,0))