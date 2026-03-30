class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left_m = 0
        right_m = m-1

        while left_m <= right_m:
            mid_m = (left_m + right_m) // 2
            if target > matrix[mid_m][n-1]:
                left_m = mid_m + 1
            elif target < matrix[mid_m][0]:
                right_m = mid_m - 1
            else:
                nth_row = mid_m
                break
        else:
            return False
        
        # if mid_m < 0:
        #     return False

        ##錯誤寫法: 首先while判斷式在輸入只有1行row時進不去，第二是都取row末位做判斷沒有將所有情況分割清楚
        # while left_m < right_m:
        #     if target < matrix[0][n-1]:
        #         nth_row = 0
        #         break
        #     #要放進迴圈內判斷，才能確保迴圈不會無限run
        #     mid_m = (left_m + right_m) // 2
        #     if target == matrix[mid_m][n-1]:
        #         return True
        #     if target < matrix[mid_m][n-1]:
        #         right_m = mid_m
        #     if target > matrix[mid_m][n-1]:
        #         left_m = mid_m + 1
        #         nth_row = left_m
        #         #因指標取的是row末端，比left_m大，代表目標在下一row
        #         #且用//時，最後一步mid_m會等於left_m
        
        left_n = 0
        right_n = n - 1
        while left_n <= right_n:
            mid_n = (left_n + right_n) // 2
            if target == matrix[nth_row][mid_n]:
                return True
            if target < matrix[nth_row][mid_n]:
                right_n = mid_n - 1
            if target > matrix[nth_row][mid_n]:
                left_n = mid_n + 1
        return False
            




            

        