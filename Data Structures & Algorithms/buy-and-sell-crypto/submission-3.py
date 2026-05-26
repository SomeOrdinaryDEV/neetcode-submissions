class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r] :
                cur = prices[r]-prices[l]
                profit = max(cur, profit)
            else:
                l = r
            r+=1

        return profit 

#[10,1,5,6,7,1]
#    i x x x x
#[10,8,7,5,2]
#  