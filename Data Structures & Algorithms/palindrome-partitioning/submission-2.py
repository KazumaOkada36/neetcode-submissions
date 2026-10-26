class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(x):
            return x == x[::-1]

        results = []
        path = []
        def dfs(i):
            if i == len(s):
                results.append(path.copy())
                return
            for j in range(i+1, len(s)+1):
                if palindrome(s[i:j]):
                    path.append(s[i:j])
                    dfs(j)
                    path.pop()

        dfs(0)
        return results


        