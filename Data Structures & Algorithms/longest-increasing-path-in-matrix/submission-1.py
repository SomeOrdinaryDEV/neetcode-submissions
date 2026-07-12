class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(i,j, prevVal):
            if (i==ROWS or j==COLS or i<0 or j<0 or matrix[i][j] <= prevVal):
                return 0
            if (i,j) in memo: 
                return memo[(i,j)]
            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))
    
            memo[(i,j)] = res
            return res
    
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,-1)
        
        return max(memo.values())
        


            
