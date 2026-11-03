class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(n):
            visited.add(n)
            for node in hashy[n]:
                if node not in visited:
                    dfs(node)
                    
            

        visited = set()
        hashy = {a: [] for a in range(n)}
        for a, b in edges:
            hashy[a].append(b)
            hashy[b].append(a)
        count = 0
        for a in range(n):
            if a not in visited:
                dfs(a)
                count += 1
        
        return count
        


        