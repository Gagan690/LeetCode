class Solution:
    def spiralOrder(self, matrix):
        result = []
        left = 0
        bottom = len(matrix)
        right = len(matrix[0])
        top = 0

        while left < right and top < bottom:
          for i in range(left, right):
            result.append(matrix[top][i])
          top += 1
          for i in range(top , bottom):
            result.append(matrix[i][right - 1])
          right -= 1
          if not (left < right and top < bottom):
            break

          for i in range(right - 1 , left - 1, -1):
            result.append(matrix[bottom - 1][i])
          bottom -= 1

          for i in range(bottom - 1 , top - 1, -1):
            result.append(matrix[i][left])
          left += 1
        return result

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
