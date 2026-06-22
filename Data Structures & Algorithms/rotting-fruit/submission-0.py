class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        time = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while fresh>0 and q:
            length = len(q)

            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col]=2
                        q.append((row,col))
                        fresh -=1
            time += 1
        return time if fresh == 0 else -1