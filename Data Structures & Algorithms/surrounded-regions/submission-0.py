class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        n, m = ROWS-1, COLS-1

        def dfs(i, j):
            if(i<0 or j<0 or i==ROWS or j==COLS
                or board[i][j]=="X" or board[i][j]=="#"
            ):
                return
            
            board[i][j]="#"

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(COLS):
            if board[0][i] == "O":
                dfs(0,i)
            if board[n][i] == "O":
                dfs(n,i)
        for j in range(ROWS):
            if board[j][0] == "O":
                dfs(j,0)
            if board[j][m] == "O":
                dfs(j,m)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="O":
                    board[i][j] = "X"
                if board[i][j]=="#":
                    board[i][j] = "O"
