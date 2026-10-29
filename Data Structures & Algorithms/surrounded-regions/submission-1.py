class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            board[i][j] = "1"
            if i>0 and board[i-1][j] == "O":
                dfs(i-1, j)
            if j>0 and board[i][j-1] == "O":
                dfs(i, j-1)
            if i<len(board)-1 and board[i+1][j]== "O":
                dfs(i+1, j)
            if j<len(board[0])-1 and board[i][j+1] == "O":
                dfs(i, j+1)

        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][len(board[0])-1] == "O":
                dfs(i, len(board[0])-1)
        for j in range(len(board[0])):
            if board[0][j] == "O":
                dfs(0, j)
            if board[len(board)-1][j] == "O":
                dfs(len(board)-1, j)
        
        for a in range(len(board)):
            for b in range(len(board[a])):
                if board[a][b] == "O":
                    board[a][b] = "X"
        for a in range(len(board)):
            for b in range(len(board[a])):
                if board[a][b] == "1":
                    board[a][b] = "O"