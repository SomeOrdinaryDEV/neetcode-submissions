class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        treasures = set()

        def dfs(i, j, distance):
            if (i<0 or j<0 or j==COLS or i==ROWS or
                grid[i][j] == -1 or distance>grid[i][j]
            ):
                return
            grid[i][j] = min(distance, grid[i][j])

            dfs(i+1, j, distance+1)
            dfs(i-1, j, distance+1)
            dfs(i, j+1, distance+1)
            dfs(i, j-1, distance+1)



        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    dfs(i,j,0)

