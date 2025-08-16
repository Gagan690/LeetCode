class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        cols = len(matrix[0])
        for m in range(row):
            for n in range(cols):
                if matrix[m][n] == target:
                    return True
        return False
