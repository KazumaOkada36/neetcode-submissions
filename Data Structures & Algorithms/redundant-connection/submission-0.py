class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(n, parent):
            if n in visited:
                potentials.append((n, parent))
        hashy = {a:[] for a in range(len(edges)+1)}
        visited = set()
        potentials = []
        for a, b in edges:
            hashy[a].append(b)
            hashy[b].append(a)
        
        dfs(-1, 0)
        return potentials[-1]
        
            