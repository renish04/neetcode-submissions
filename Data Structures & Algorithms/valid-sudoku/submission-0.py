class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            temp = []
            for j in range(len(board)):
                if board[i][j] != ".":
                    temp.append(board[i][j])
            temp_set = set(temp)
            
            if len(temp_set) != len(temp):
                return False

        for j in range(len(board)):
            temp = []
            for i in range(len(board)):
                if board[i][j] != ".":
                    temp.append(board[i][j])
            temp_set = set(temp)
            
            if len(temp_set) != len(temp):
                return False
        
        i = 0
        j = 0
        while i < len(board):
            while j < len(board):
                temp = []
                if board[i][j] != ".":
                    temp.append(board[i][j])
                if board[i][j+1] != ".":
                    temp.append(board[i][j+1])
                if board[i][j+2] != ".":
                    temp.append(board[i][j+2])
                if board[i+1][j] != ".":
                    temp.append(board[i+1][j])
                if board[i+1][j+1] != ".":
                    temp.append(board[i+1][j+1])
                if board[i+1][j+2] != ".":
                    temp.append(board[i+1][j+2])
                if board[i+2][j] != ".":
                    temp.append(board[i+2][j])
                if board[i+2][j+1] != ".":
                    temp.append(board[i+2][j+1])
                if board[i+2][j+2] != ".":
                    temp.append(board[i+2][j+2])
                temp_set = set(temp)
                
                if len(temp_set) != len(temp):
                    return False
                j += 3
            i += 3

        return True