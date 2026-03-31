class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        max_size = 0

        def dfs(r, c):
            stack = [(r, c)]
            area = 0

            while stack:
                row, col = stack.pop()
                if (row < 0 or col < 0 or row >= ROWS or col >= COLS 
                    or grid[row][col] == 0):
                    continue

                grid[row][col] = 0
                area += 1

                for dr, dc in directions:
                    stack.append((row + dr, col + dc))

            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_size = max(max_size, dfs(i, j))

        return max_size
        