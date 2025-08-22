class Solution:
    def isPerfectSquare(self, num):
        if num%(num**0.5)==0:
            return True
        return False
