class Solution:
    def maxProfit(self, prices):
        maxsell = 0
        minbuy = prices[0]
        for i in prices:
            minbuy = min(minbuy,i)
            maxsell = max(maxsell, i-minbuy)

        return maxsell
