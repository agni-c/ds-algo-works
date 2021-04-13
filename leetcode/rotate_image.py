class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # swapping upside down
        for j in range(n):
            for i in range(n//2):
                matrix[i][j],matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        # swapping diagonally
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
        return matrix   