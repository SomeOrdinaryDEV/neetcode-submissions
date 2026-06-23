class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        preMap = {i: [] for i in range(n)}
        for s,d in edges:
            preMap[s].append(d)
            preMap[d].append(s)
        visit = set()
        def dfs(i, par):
            if i in visit:
                return False
            
            visit.add(i)
            for pre in preMap[i]:
                if pre == par:
                    continue
                if not dfs(pre, i):
                    return False
            return True


        return dfs(0,-1) and len(visit) == n