class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        NOT_surrounded = set()
        def dfs(y, x):
            if y < 0 or y >= ROWS or x < 0 or x >= COLS:
                return
            if board[y][x] == 'X':
                return
            if (y, x) in NOT_surrounded:
                return
            NOT_surrounded.add((y, x))
            dfs(y+1, x)
            dfs(y-1, x)
            dfs(y, x+1)
            dfs(y, x-1)
        
        for i in range(ROWS):
            dfs(i, 0)         #第一次錯寫:dfs(i, 1)
            dfs(i, COLS-1)
        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS-1, j)
        
        for k in range(ROWS):
            for l in range(COLS):
                if board[k][l] == 'O' and (k, l) not in NOT_surrounded:
                    board[k][l] = 'X'  #第一次錯寫: board[k][l] == 'X'
        

            
        
        