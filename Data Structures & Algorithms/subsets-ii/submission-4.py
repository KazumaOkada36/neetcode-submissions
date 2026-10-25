class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        def dfs(i, listy):
            if i == len(nums):
                results.append(listy.copy())
                return
            listy.append(nums[i])
            dfs(i+1, listy)
            listy.pop()
            j = i + 1
            while j<len(nums) and nums[i] == nums[j]:
                j += 1
            dfs(j, listy)
        
        dfs(0, [])
        return results
        
        