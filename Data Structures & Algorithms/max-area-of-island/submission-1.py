class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                sumy = 1
                if i<len(grid)-1:
                    sumy += dfs(i+1, j)
                if j<len(grid[0])-1:
                    sumy += dfs(i, j+1)
                if i>0:
                    sumy += dfs(i-1, j)
                if j>0:
                    sumy += dfs(i, j-1)
                return sumy




        maxy = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxy = max(maxy, dfs(i, j))

        return maxy

        
        