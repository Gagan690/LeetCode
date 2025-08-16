class Solution:
    def transpose(self, matrix):
        row , cols = len(matrix) , len(matrix[0])
        result = [[0 for _ in range(row)] for _ in range(cols)]
        for i in range(row):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        return result
