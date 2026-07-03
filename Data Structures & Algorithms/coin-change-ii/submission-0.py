class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        def ways(amt, coins, i):
            key = (amt, i)
            
            if key in memo:
                return memo[key]
            if amt == 0:
                return 1
            if i==len(coins):
                return 0
            coin = coins[i]
            total_ways = 0
            for qty in range(0, (amt//coin)+1):
                remainder = amt - (coin*qty)
                total_ways += ways(remainder, coins, i+1)
            memo[key] = total_ways
            return total_ways
        return ways(amount, coins, 0)
        

