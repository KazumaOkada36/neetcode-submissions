class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def dfs(stringy, close_count, open_count):
            if len(stringy) == 2*n:
                results.append(stringy)
                return
            if open_count< n:
                dfs(stringy + "(", close_count, open_count+1)
            if close_count < open_count:
                dfs(stringy + ")", close_count+1, open_count)
        
        dfs("", 0, 0)            

        return results

        