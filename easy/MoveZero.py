class Solution:
  def moveZeroes(self, nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in nums:
      if i == 0:
        nums.remove(i)
        nums.append(i)
