class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for i in graph[node]:
                if i == parent:
                    continue
                else:
                    if not dfs(i):
                        return False
            visited.remove(node)
        
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        if not dfs(0, -1):
            return False
        
        return len(visted) == n