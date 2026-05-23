class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            check_set = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in check_set:
                       
                        return False
                    else:
                        check_set.add(board[i][j])
        
        for i in range(len(board)):
            check_set = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] in check_set:
                        
                        return False
                    else:
                        check_set.add(board[j][i])
        i = 0
        while i < len(board):
            
            j = 0
            while j < len(board):
                check_set = set()
                if board[i][j] in check_set:
                    
                    return False
                elif board[i][j] not in check_set and board[i][j] != ".":
                    check_set.add(board[i][j])
                if board[i][j+1] in check_set:
                   
                    return False
                elif board[i][j+1] not in check_set and board[i][j+1] != ".":
                    check_set.add(board[i][j+1])
                if board[i][j+2] in check_set:
                   
                    return False
                elif board[i][j+2] not in check_set and board[i][j+2] != ".":
                    check_set.add(board[i][j+2])
                if board[i+1][j] in check_set:
                    
                    return False
                elif board[i+1][j] not in check_set and board[i+1][j] != ".":
                    check_set.add(board[i+1][j])
                if board[i+1][j+1] in check_set:
                    
                    return False
                elif board[i+1][j+1] not in check_set and board[i+1][j+1] != ".":
                    check_set.add(board[i+1][j+1])
                if board[i+1][j+2] in check_set:
                    
                    return False
                elif board[i+1][j+2] not in check_set and board[i+1][j+2] != ".":
                    check_set.add(board[i+1][j+2])
                if board[i+2][j] in check_set:
                   
                    return False
                elif board[i+2][j] not in check_set and board[i+2][j] != ".":
                    check_set.add(board[i+2][j])
                if board[i+2][j+1] in check_set:
                   
                    return False
                elif board[i+2][j+1] not in check_set and board[i+2][j+1] != ".":
                    check_set.add(board[i+2][j+1])
                
                if board[i+2][j+2] in check_set:
                  
                    return False
                elif board[i+2][j+2] not in check_set and board[i+2][j+2] != ".":
                    check_set.add(board[i+2][j+2])
                j += 3
            i += 3
        
        return True