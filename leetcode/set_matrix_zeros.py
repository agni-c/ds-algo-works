class Solution:
    # m+n soloutions
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_size = len(matrix)
        col_size = len(matrix[0])

        ROW = ["*"]*row_size
        COL = ["*"]*col_size

       
        for row in range(row_size):
            for col in range(col_size):

                if matrix[row][col] == 0:
                    ROW[row]=0
                    COL[col]=0
                    
        print(ROW,COL)
        for row in range(row_size):
            for col in range(col_size):
                if ROW[row]==0 or COL[col]==0:
                    matrix[row][col] =0

    # constant space soloutions
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_size = len(matrix)
        col_size = len(matrix[0])
        
        row_zero = False
        col_zero = False
        
        for row in range(row_size): 
            if matrix[row][0] == 0:
                row_zero = True
                break
            
        for col in range(col_size): 
            if matrix[0][col] == 0:
                col_zero = True
                break
            
            
        for row in range(1,row_size):
            for col in range(1,col_size):
                if matrix[row][col]==0:
                    matrix[row][0]=0
                    matrix[0][col]=0
                             
        for row in range(1,row_size):
            for col in range(1,col_size):
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col]=0
        
        if row_zero:
            for row in range(row_size):
                matrix[row][0]=0
        if col_zero:
            for col in range(col_size):
                matrix[0][col]=0