class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(candidates)

        def dfs(i, sol, total):
            if total == target:
                res.append(sol.copy())
                return
            if total > target or i == n:
                return 
            
            sol.append(candidates[i])
            dfs(i+1,sol, total+candidates[i])
            sol.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, sol, total)

        candidates.sort()
        dfs(0, [], 0)
        return [list(s) for s in res]
            