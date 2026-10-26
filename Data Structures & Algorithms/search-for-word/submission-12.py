class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            temp = board[i][j]
            board[i][j] = "#"
            if i<len(board)-1 and board[i+1][j] == word[k+1]:
                if dfs(i+1, j, k+1):
                    return True
            if j< len(board[0])-1 and board[i][j+1] == word[k+1]:
                if dfs(i, j+1, k+1):
                    return True
            if i>0 and board[i-1][j] == word[k+1]:
                if dfs(i-1, j, k+1):
                    return True
            if j>0 and board[i][j-1] == word[k+1]:
                if dfs(i, j-1, k+1):
                    return True
            board[i][j] = temp
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        
        return False
        
    
