class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashy = set()
        if len(nums) == 0:
            return 0
            
        for num in nums:
            hashy.add(num)

        i = 0
        j = 0
        num = min(hashy)
        while hashy:
            if num in hashy:
                looking_for_num = num+1
                hashy.remove(num)
                j += 1
                num = looking_for_num
            else:
                num = min(hashy)
                j = 0
            if j > i:
                i = j

        return i





