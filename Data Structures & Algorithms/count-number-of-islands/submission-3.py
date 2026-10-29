class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i<len(grid)-1:
                    dfs(i+1, j)
                if j<len(grid[0])-1:
                    dfs(i, j+1)
                if i>0:
                    dfs(i-1, j)
                if j>0:
                    dfs(i, j-1)
                return True
            else:
                return


        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if dfs(i, j) == True:
                    count += 1
        
        return count
