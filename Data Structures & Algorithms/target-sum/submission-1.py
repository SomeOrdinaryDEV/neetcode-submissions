class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(i, sum):
            if i == len(nums):
                return sum == target
            
            return dfs(i+1, sum-nums[i]) + dfs(i+1, sum+nums[i])
        
        return dfs(0,0)


