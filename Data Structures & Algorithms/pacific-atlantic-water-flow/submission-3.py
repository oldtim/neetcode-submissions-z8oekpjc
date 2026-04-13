class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))

        pac = [[False]*COLS for _ in range(ROWS)]
        atl = [[False]*COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque()
            
            for r, c in source:
                ocean[r][c] = True
                q.append((r, c))
            
            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]):
                        
                        ocean[nr][nc] = True   # 🔥 提前標記
                        q.append((nr, nc))

        pacific = [(0,c) for c in range(COLS)] + [(r,0) for r in range(ROWS)]
        atlantic = [(ROWS-1,c) for c in range(COLS)] + [(r,COLS-1) for r in range(ROWS)]

        bfs(pacific, pac)
        bfs(atlantic, atl)

        return [[r,c] for r in range(ROWS) for c in range(COLS) if pac[r][c] and atl[r][c]]
                