class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        def head_right(i,j):
            #if matrix[i][j] > 100 or j >= len(matrix[0]):
            if j >= len(matrix[0]) or matrix[i][j] > 100 :
                return
            for right in range(j, len(matrix[0])):
                if matrix[i][right] > 100:
                    right -= 1
                    break
                ans.append(matrix[i][right])
                matrix[i][right] = 101
            head_down(i+1, right)
        
        def head_down(i,j):
            if i >= len(matrix) or matrix[i][j] > 100:
                return
            for down in range(i, len(matrix)):
                if matrix[down][j] > 100:
                    down -= 1
                    break
                ans.append(matrix[down][j])
                matrix[down][j] = 101
            head_left(down, j-1)

        def head_left(i,j):
            if j < 0 or matrix[i][j] > 100:
                return
            for left in range(j, -1, -1):
                if matrix[i][left] > 100:
                    left += 1      # 錯誤2.
                    break
                ans.append(matrix[i][left])
                matrix[i][left] = 101
            head_up(i-1, left)
        
        def head_up(i,j):
            if i < 0 or matrix[i][j] > 100:
                return
            for up in range(i, -1, -1):
                if matrix[up][j] > 100:
                    up += 1
                    break
                ans.append(matrix[up][j])
                matrix[up][j] = 101
            head_right(up, j+1)
        
        head_right(0,0)
        return ans

                

            


        



    
        