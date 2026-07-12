class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(i, sum):
            if i == len(nums):
                return sum == target
            if (i,sum) in memo:
                return memo[(i,sum)]
            

            memo[(i, sum)] = dfs(i+1, sum-nums[i]) + dfs(i+1, sum+nums[i])
            return memo[(i,sum)]
        return dfs(0,0)


