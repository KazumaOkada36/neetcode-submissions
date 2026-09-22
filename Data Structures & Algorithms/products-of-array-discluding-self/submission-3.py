class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_listy = []
        suffix_listy = [1] * len(nums)
        product = 1
        for num in nums:
            prefix_listy.append(product)
            product *= num
        
        for i in range(len(nums)-2, -1, -1):
            suffix_listy[i] = suffix_listy[i+1] * nums[i+1]
        
        real_listy = [1] * len(nums)
        for i in range(len(nums)):
            real_listy[i] = prefix_listy[i]*suffix_listy[i]
        
        return real_listy

        

