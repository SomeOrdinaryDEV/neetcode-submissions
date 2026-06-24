class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l1 = nums[:-1]
        l2 = nums[1:]
        memo1 = [-1] * len(l1)
        memo2 = [-1] * len(l2)

        def dfs(i, l, m):
            if i>=len(l):
                return 0
            if m[i] != -1:
                return m[i]
            m[i] = max(dfs(i+1, l, m), l[i]+dfs(i+2, l, m))
            return m[i]

        cost = max(dfs(0,l1,memo1), dfs(0,l2,memo2))   
        return cost