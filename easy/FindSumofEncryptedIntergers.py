class Solution:
    def encrypt(self, x):
        lst = list(map(int, str(x)))
        return int(str(max(lst)) * len(str(x)))

    def sumOfEncryptedInt(self, nums) -> int:
        result = 0
        for i in nums:
            result += self.encrypt(i)
        return result
