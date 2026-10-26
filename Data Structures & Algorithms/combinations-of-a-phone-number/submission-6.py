class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        results = []
        hashy = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}
        stringy = []
        def dfs(i):
            if i == len(digits):
                results.append("".join(stringy))
                return 
            digity = int(digits[i])
            for j in hashy[digity]:
                stringy.append(j)
                dfs(i+1)
                stringy.pop()
        
        dfs(0)
        return results
        