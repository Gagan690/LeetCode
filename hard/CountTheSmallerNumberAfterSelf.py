class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        index += 1  # 1-based indexing
        while index <= self.size:
            self.tree[index] += value
            index += index & (-index)

    def query(self, index):
        index += 1  # 1-based indexing
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & (-index)
        return sum_val

class Solution:
    def countSmaller(self, nums):
        # Coordinate compression
        sorted_nums = sorted(list(set(nums)))
        rank_map = {num: i for i, num in enumerate(sorted_nums)}

        n = len(nums)
        result = [0] * n
        size = len(sorted_nums)
        ft = FenwickTree(size)

        for i in range(n - 1, -1, -1):
            rank = rank_map[nums[i]]
            result[i] = ft.query(rank - 1)
            ft.update(rank, 1)

        return result

# class Solution:
#     def countSmaller(self, nums):
#         result = []
#         for i in range(len(nums)):
#             output = 0
#             for j in range(i+1, len(nums)):
#                 if nums[i] < nums[j]:
#                     output += 1
#             result.append(output)
#         return result

# class Solution:
#   def countSmaller(self, nums):
#     sorted_nums = sorted(nums)
#     result = []
#     for num in nums:
#       result.append(sorted_nums.index(num))
#       sorted_nums.remove(num)
#     return result

print(Solution().countSmaller([5,2,6,1]))


print(Solution().countSmaller([5,2,6,1]))
print(Solution().countSmaller([-1,-1]))
