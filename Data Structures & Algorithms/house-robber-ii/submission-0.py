class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(house):
            dp = [0]*len(house)
            dp[0] = house[0]
            dp[1] = max(house[0],house[1])
            for i in range(2, len(house)-1):
                dp[i] = max(dp[i-1], dp[i-2] + house[i])
            
            return dp[-1]
        
        return max(helper(nums[1:]), helper(nums[:-1]))
            
        
        