class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for k in range(len(nums)):
            hashy[nums[k]] = k
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashy.keys():
                if hashy[difference] != i:
                    return [i, hashy[difference]]