class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, index):
            if index == len(word):
                return True
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[index] != board[r][c] or
                (r, c) in visit):
                return False
            
            visit.add((r,c))
            res = (dfs(r+1,c,index+1) or
                    dfs(r-1,c,index+1) or
                    dfs(r,c+1,index+1) or
                     dfs(r,c-1,index+1))
            visit.remove((r,c))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False
