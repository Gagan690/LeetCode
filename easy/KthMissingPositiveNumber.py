class Solution:
  def findKthPositive(self, arr, k: int) -> int:
    missing = []
    count = 1
    while len(missing) != k:
      if count not in arr:
        missing.append(count)
      count += 1
    return missing[-1]
