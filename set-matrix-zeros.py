class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrows = len(matrix)
        ncols = len(matrix[0])
        row0 = -1
        
        # print (nrows, ncols)
        
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        row0 = 0
                    else:                        
                        matrix[i][0] = 0
                        
        # print (matrix)
                        
        for i in range(nrows):
            for j in range(ncols):
                if i > 0 and j > 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(nrows):
                matrix[i][0] = 0
        
        if row0 == 0:
            for j in range(ncols):
                matrix[0][j] = 0
                    
        
