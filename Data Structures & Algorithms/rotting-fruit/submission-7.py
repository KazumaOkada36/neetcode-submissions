from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        count = -1
        while queue:
            for num in range(len(queue)):
                i, j = queue.popleft()
                if i>0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append((i-1, j))
                if j>0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    queue.append((i, j-1))
                if i<len(grid)-1 and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append((i+1, j))
                if j<len(grid[0])-1 and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    queue.append((i, j+1))
            count += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return max(0, count)


        

        