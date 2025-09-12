# class Solution:
#     def countRangeSum(self, nums, lower, upper):
#         perfix = 0
#         store = [0]
#         for i in range(len(nums)):
#             perfix += nums[i]
#             store.append(perfix)
#         count = 0
#         i = 0
#         while i <= len(store):
#             for j in range(i+1,len(store)):
#                 total = store[j] - store[i]
#                 if total >= lower and total <= upper:
#                     count += 1
#             i += 1
#         #for i in range(0,len(store)-1):
#            # for j in range(i+1,len(store)):
#           #      total = store[j] - store[i]
#          #       if total >= lower and total <= upper:
#         #            count += 1
#         return count

# print(Solution().countRangeSum([-2,5,-1],-2,2))


class Solution:
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        def merge_sort(arr, left, right):
            if left == right:
                return 0

            mid = (left + right) // 2
            count = merge_sort(arr, left, mid) + merge_sort(arr, mid + 1, right)

            j = mid + 1
            k = mid + 1
            for i in range(left, mid + 1):
                while j <= right and arr[j] - arr[i] < lower:
                    j += 1
                while k <= right and arr[k] - arr[i] <= upper:
                    k += 1
                count += (k - j)

            # Merge the two sorted halves
            merged = []
            l, r = left, mid + 1
            while l <= mid and r <= right:
                if arr[l] <= arr[r]:
                    merged.append(arr[l])
                    l += 1
                else:
                    merged.append(arr[r])
                    r += 1
            merged.extend(arr[l:mid + 1])
            merged.extend(arr[r:right + 1])
            arr[left:right + 1] = merged

            return count

        return merge_sort(prefix_sum, 0, n)

# Example Usage:
print(Solution().countRangeSum([-2,5,-1],-2,2))
