class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        effort = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if effort[i] != -1:
                return effort[i]
            
            one = cost[i] + dfs(i+1)
            two = cost[i] + dfs(i+2)

            effort[i] = min(one, two)

            return effort[i]
        
        return min(dfs(0), dfs(1))
            