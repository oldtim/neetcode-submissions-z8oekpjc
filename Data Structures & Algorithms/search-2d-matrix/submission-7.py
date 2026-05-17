class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #見solution內，Binary Search (One Pass)部分，將整個矩陣視為一個array

        m = len(matrix)
        n = len(matrix[0])
        left = matrix[0][0]
        left_n = 0
        right = matrix[m-1][n-1]
        right_n = m*n - 1
        while left_n <= right_n:
            mid_n = (left_n + right_n)//2
            if (mid_n + 1)%n != 0:
                mid = matrix[(mid_n + 1)//n][(mid_n + 1)%n - 1]
            else:
                mid = matrix[(mid_n + 1)//n - 1][-1]
                
            if target > mid:
                left_n = mid_n + 1
            elif target < mid:
                right_n = mid_n - 1
            else:
                return True
        
        return False



        