class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n%2 == 0:
            for y in range(n//2):
                for x in range(n//2):   
                    temp = matrix[(n//2)+x][(n//2)+y]
                    matrix[(n//2)+x][(n//2)+y] = matrix[(n//2 - 1)-y][(n//2)+x]
                    temp2 = matrix[(n//2)+y][(n//2 - 1)-x]
                    matrix[(n//2)+y][(n//2 - 1)-x] = temp
                    temp3 = matrix[(n//2 - 1)-x][(n//2 - 1)-y]
                    matrix[(n//2 - 1)-x][(n//2 - 1)-y] = temp2
                    matrix[(n//2 - 1)-y][(n//2)+x] = temp3

        if n%2 == 1:
            for y in range(1, n//2 + 1):
                for x in range(n//2 + 1):
                    temp = matrix[(n//2)+x][(n//2)+y]
                    matrix[(n//2)+x][(n//2)+y] = matrix[(n//2)-y][(n//2)+x]
                    temp2 = matrix[(n//2)+y][(n//2)-x]
                    matrix[(n//2)+y][(n//2)-x] = temp
                    temp3 = matrix[(n//2)-x][(n//2)-y]
                    matrix[(n//2)-x][(n//2)-y] = temp2
                    matrix[(n//2)-y][(n//2)+x] = temp3               

        #(i,j)->(j,-i)->(-i,-j)->(-j,i)