class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        PA_Ocean = [0, 0]
        ans = []
        visited = set()
        def FindSea(y, x, pre_height):
            if (y, x) in visited:
                return
            if y < 0 or x < 0:
                PA_Ocean[0] = 1
                return
            if y >= ROWS or x >= COLS:
                PA_Ocean[1] = 1
                return
            if heights[y][x] > pre_height:
                return

            visited.add((y, x))    
            for dr in directions:
                FindSea(y+dr[0], x+dr[1], heights[y][x])
        
        for i in range(ROWS):
            for j in range(COLS):
                PA_Ocean = [0, 0]
                visited = set()
                FindSea(i, j, heights[i][j])
                if PA_Ocean == [1, 1]:
                    ans.append([i, j])
        
        return ans

#第一次寫，沒加上visited，所以遇到鄰近方塊height相等時，可以不斷來回流動->跑不完


        
        