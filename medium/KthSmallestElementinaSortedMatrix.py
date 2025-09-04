class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        result = []
        for i in range(len(matrix)):
            result += matrix[i]
        result = sorted(result)
        # print(result)
        return result[k-1]

# print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))

# print(Solution().kthSmallest([[1,2],[1,3]],2))
