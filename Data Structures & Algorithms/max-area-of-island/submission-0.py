class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        max_size = 0

        def dfs(r,c):
            if (r<0 or c<0 or r>=ROWS or c>=COLS 
                or grid[r][c] == 0):
                return
            grid[r][c] = 0
            nonlocal tmp_size
            tmp_size += 1
            for dr, dc in directions:
                dfs(r+dr,c+dc)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    tmp_size = 0
                    dfs(i,j)
                    max_size = max(max_size, tmp_size)
        return max_size
        