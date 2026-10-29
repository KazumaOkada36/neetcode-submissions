class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()

        def dfs(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            if i>0 and heights[i-1][j]>=heights[i][j]:
                dfs(i-1, j, visited)
            if j>0 and heights[i][j-1]>=heights[i][j]:
                dfs(i, j-1, visited)
            if i<len(heights)-1 and heights[i+1][j]>=heights[i][j]:
                dfs(i+1, j, visited)
            if j<len(heights[0])-1 and heights[i][j+1]>=heights[i][j]:
                dfs(i, j+1, visited)

        for k in range(len(heights[0])):
            dfs(0, k, pacific)
            dfs(len(heights)-1, k, atlantic)
        for j in range(len(heights)):
            dfs(j, 0, pacific)
            dfs(j, len(heights[0])-1, atlantic)

        listy = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i, j) in atlantic:
                    listy.append([i, j])
        
        return listy
        



        