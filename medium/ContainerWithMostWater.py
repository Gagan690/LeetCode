class Solution:
    def maxArea(self, height) -> int:
        result = 0
        l, r = 0 , len(height) - 1
        while l != r:
            min_height = min(height[l],height[r])
            difference = abs(l - r)
            if min_height * difference > result:
                result = min_height * difference

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return result
