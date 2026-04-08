class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        steps = [[0,1], [0,-1], [1,0], [-1,0]]

        def access_island(y, x, r):
            if y >= ROWS or x >= COLS or y < 0 or x < 0:
                return
            if grid[y][x] == -1:
                return
            if grid[y][x] == 0 and r != 0:
                return
            if grid[y][x] > 0 and r >= grid[y][x]:
                return
            else:
                grid[y][x] = r
           
            for next_step in steps:
                new_y = y + next_step[0]
                new_x = x + next_step[1]
                #錯誤1.:在此處修改r，會讓四個方向的r增量不一樣
                # r += 1
            
                #錯誤2.:應放在def剛開始判斷並擋回超出範圍，放在此grid值會直接不存在
                # if grid[new_y][new_x] and grid[new_y][new_x] == 0 and r != 0:
                #     continue
                # else:
                access_island(new_y, new_x, r+1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    access_island(i, j, 0)



            

        


        