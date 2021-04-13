class Solution(object):
    def exist(self, board, word):
        
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if word[0]==board[i][j] and self.search(i,j,0,word,board):
                    return True
        return False
    
    def search(self,i,j,count,word,board):
        if len(word)==count:
            return True
        if (i<0 or i>=len(board) or j<0 or j>=len(board[0])) or( board[i][j] != word[count]):
            return False
        temp = board[i][j] 
        board[i][j]="*"
        flag = self.search(i+1,j,count+1,word,board) or self.search(i-1,j,count+1,word,board) or self.search(i,j+1,count+1,word,board) or self.search(i,j-1,count+1,word,board)
        board[i][j]=temp
        return flag
        
            

    

                    