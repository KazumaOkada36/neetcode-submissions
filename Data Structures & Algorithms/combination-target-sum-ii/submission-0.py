class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(i, listy, sumy):
            if sumy == target:
                result.append(listy.copy())
                return
            if sumy > target:
                return
            if i == len(candidates):
                return
            
            listy.append(candidates[i])
            dfs(i+1, listy, sumy+candidates[i])
            listy.pop()
            j = i+1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, listy, sumy)

        dfs(0, [], 0)
        return result

