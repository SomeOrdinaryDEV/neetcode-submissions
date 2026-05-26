class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(9)]
        rows = [[] for _ in range(9)]
        grid = [[list() for _ in range(3)] for _ in range(3)]

        for i in range(0,9):
            for j in range(0,9):
                num = board[i][j]
                if num == ".":
                    continue
                
                if num in rows[i] or num in cols[j] or num in grid[i//3][j//3]:
                    return False
                rows[i].append(num)
                cols[j].append(num)
                grid[i//3][j//3].append(num)
        return True
        


