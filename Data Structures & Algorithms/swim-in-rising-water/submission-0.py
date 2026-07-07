import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        visit = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        minH = [[grid[0][0], 0,0]]
        visit.add((0,0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return t
            for dr, dc in directions:
                x,y = r+dr, c+dc
                if (min(x,y) <0 or x==N or y==N or
                    (x,y) in visit    
                    ):
                    continue
                visit.add((x,y))
                heapq.heappush(minH, [max(t, grid[x][y]), x, y])