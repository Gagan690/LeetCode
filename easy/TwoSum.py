class Solution:
    def twoSum(self, nums, target):
      prevMap = {}
      for i , n in enumerate(nums):
        deff = target - n
        if deff in prevMap:
          return [prevMap[deff],i]
        prevMap[n] = i
      return
