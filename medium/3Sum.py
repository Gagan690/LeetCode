class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum < 0:
                    l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         for i in range(0,len(nums)-2):
#             for k in range(i+1,len(nums)-1):
#                 for j in range(k+1, len(nums)):
#                     if nums[i] + nums[k] + nums[j] == 0:
#                         result.append([nums[i] , nums[k] , nums[j]])
#         unique_result = set()
#         for i in result:
#             unique_result.add(tuple(sorted(i)))
#         return [list(i) for i in unique_result]
