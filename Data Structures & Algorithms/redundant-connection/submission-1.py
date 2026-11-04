class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(n, target):
            if n == target:
                return True 
            for a in hashy[n]:
                if a not in visited:
                    if dfs(a, target):
                        return True
            return False
        
        hashy = {a:[] for a in range(len(edges)+1)}
        for a, b in edges:
            visited = set()
            if dfs(a, b):
                return [a, b]
            hashy[a].append(b)
            hashy[b].append(a)
        
    
        
            