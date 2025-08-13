class SolutionOriginal:
    def containsNearbyDuplicate(self, nums, k):
        """
        Original O(n²) solution - SLOW
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False


  class SolutionSlidingWindow:
    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return False
        window = set()

        for i, num in enumerate(nums):
            if i > k:
                window.remove(nums[i - k - 1])
            if num in window:
                return True
            window.add(num)

        return False
