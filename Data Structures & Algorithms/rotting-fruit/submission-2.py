class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # visited = set()  
        q = deque()
        def AddCell(y, x):
            if y >= ROWS or x >= COLS or y < 0 or x < 0:
                return
            if grid[y][x] == 0 or grid[y][x] == 2:
                return
            # if (y,x) in visited:
            #     return
            # visited.add((y,x))
            grid[y][x] = 2
            q.append([y,x])
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    # visited.add((i,j))
                    q.append([i,j])
        
        min_pass = 0
        while q:
            for _ in range(len(q)):
                y, x = q.popleft()
                # grid[y][x] = 2
                AddCell(y+1, x)
                AddCell(y-1, x)
                AddCell(y, x-1)
                AddCell(y, x+1)
            if q:
                min_pass += 1
            # min_pass += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return min_pass


                    
            
            
        
        