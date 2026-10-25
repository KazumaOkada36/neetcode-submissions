class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        listy = []
        path = []
        def dfs(i):
            sumy = 0
            for num in path:
                sumy += num
            if sumy == target:
                listy.append(path.copy())
                return
            if sumy > target:
                return
            if i == len(nums):
                return
            path.append(nums[i])
            dfs(i)
            path.pop()
            dfs(i +1)
        
        dfs(0)
        return listy