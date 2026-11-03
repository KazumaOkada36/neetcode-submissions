class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for i in graph[node]:
                if not dfs(i):
                    return False
            visited.remove(node)
        
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(a)
            graph[b].append(b)

        for k in range(n):
            if not dfs(k):
                return False
        return True
            