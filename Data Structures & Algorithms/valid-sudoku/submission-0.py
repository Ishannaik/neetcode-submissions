class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num!= ".":
                    if num in seen:
                        return False
                    seen.add(num)
        
        for col in range(9):
            seen = set()
            for row in board:
                num = row[col]
                if num!='.':
                    if num in seen:
                        return False
                    seen.add(num)
        
        
        
        for start_row in range(0,9,3):
            for start_col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[start_row+i][start_col+j]
                        if num !=".":
                            if num in seen:
                                return False
                            seen.add(num)
        return True
                
