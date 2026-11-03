class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(n):
            if n in visited:
                return True
            visited.add(n)
            for node in hashy[n]:
                if dfs(node):
                    return True
            del hashy[n]

        visited = set()
        hashy = {a: [] for a in range(n)}
        for a, b in edges:
            hashy[a].append(b)
            hashy[b].append(a)
        count = 0
        for a in range(n):
            if a not in visited:
                dfs(a)
        
        return count
        


        