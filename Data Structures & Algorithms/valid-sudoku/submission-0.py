class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            dupCheckRow={}
            for j in range(9):
                if board[i][j] !='.':
                    if board[i][j] not in dupCheckRow:
                        dupCheckRow[board[i][j]]=1
                    else:
                        return False
            dupCheckRow.clear()
        for j in range(9):
            dupCheckCol={}
            for i in range(9):
                if board[i][j] !='.':
                    if board[i][j] not in dupCheckCol:
                        dupCheckCol[board[i][j]]=1
                    else:
                        return False
            dupCheckCol.clear()
        k=0
        while k<7:
            l=0
            while l<7:
                dupCheckSquare={}
                for i in range(k,k+3):
                    for j in range(l,l+3):
                        if board[i][j] !='.':
                            if board[i][j] not in dupCheckSquare:
                                dupCheckSquare[board[i][j]]=1
                            else:
                                return False
                l+=3
            dupCheckSquare.clear()   
            k+=3
        return True
            

        

        
            