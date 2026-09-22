class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()

            for num in row:
                if num == ".":
                    continue
                elif num in seen:
                    return False
                
                seen.add(num)

        for j in range(9):
            seen = set()
            for i in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                elif num in seen:
                    return False
                
                seen.add(num)

        
        for row in (0, 3, 6):
            for column in (0, 3, 6):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[row+i][column+j]
                        if num == ".":
                            continue
                        elif num in seen:
                            return False
                
                        seen.add(num)
    
        return True


