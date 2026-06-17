class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_set = [0]*len(matrix)
        column_set = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_set[i] = 1
                    column_set[j] = 1
        
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if row_set[m] == 1 or column_set[n] == 1:
                    matrix[m][n] = 0
        
        