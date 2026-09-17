class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        adj = collections.defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u) 
        
        seen = [False] * n

        def dfs(node):
            if seen[node]:
                return
            seen[node] = True
            for nei in adj[node]:
                dfs(nei)
        
        count = 0
        for i in range(n):
            if not seen[i]:
                count += 1
                dfs(i)
        return count