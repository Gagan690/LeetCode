import bisect
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis_tails = []
        for _, height in envelopes:
            idx = bisect.bisect_left(lis_tails, height)
            if idx == len(lis_tails):
                lis_tails.append(height)
            else:
                lis_tails[idx] = height
        return len(lis_tails)


# class Solution:
#     def maxEnvelopes(self, envelopes) -> int:
#         envelopes.sort()
#         mini = min(envelopes)
#         count = 0
#         for i in range(1,len(envelopes)):
#             if envelopes[i] > mini:
#                 count += 1
#                 mini = envelopes[i]
#         if count == 0:
#           return 1
#         return count


# print(Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
# print(Solution().maxEnvelopes([[1,1],[1,1],[1,1]]))
