class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(n):
            if n in visited:
                return True
            for node in hashy[n]:
                if dfs(node):
                    return True
            visited.remove(n)
            del hashy[n]

        visited = set()
        hashy = {a: [] for a in range(n)}
        for a, b in edges:
            hashy[a].append(b)
            hashy[b].append(a)
        count = 0
        while hashy:
            for a in hashy.keys():
                if dfs(a):
                    count += 1
        
        return count
        


        