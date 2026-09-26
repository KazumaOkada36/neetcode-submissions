class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        listy = []
        for n in range(len(nums)):
            target = 0 - nums[n]
            i, j = n+1, len(nums)-1
            if n>0 and nums[n] == nums[n-1]:
                continue
            while i < j:
                if nums[i] + nums[j] == target:
                    listy.append([nums[i], nums[j], nums[n]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                           
            
        return listy
