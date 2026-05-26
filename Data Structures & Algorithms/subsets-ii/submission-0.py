class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        n = len(nums)
        def backtrack(i, sol):
            if i == n:
                res.add(tuple(sol))
                return
            
            sol.append(nums[i])
            backtrack(i+1, sol)
            sol.pop()
            backtrack(i+1, sol)


        nums.sort()
        backtrack(0,[])
        return [list(s) for s in res]
