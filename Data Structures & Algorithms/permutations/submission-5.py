class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def dfs(listy):
            if len(listy) == len(nums):
                results.append(listy.copy())
                return
            for k in range(len(nums)):
                if nums[k] not in listy:
                    listy.append(nums[k])
                    dfs(listy)
                    listy.pop()

        dfs([])
        
        return results