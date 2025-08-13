class Solution:
    def twoSum(self, numbers, target):
        l, r = 0 , len(numbers) - 1

        while l < r:
            cumSum = numbers[l] + numbers[r]
            if cumSum > target:
                r -= 1
            elif cumSum < target:
                l += 1
            else:
                return [l +1 , r+1]
