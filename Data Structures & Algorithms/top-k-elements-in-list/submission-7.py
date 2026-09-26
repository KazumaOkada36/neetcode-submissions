class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy = {}
        for num in nums:
            if num in hashy:
                hashy[num] += 1
            else:
                hashy[num] = 1
        
        result = []
        
        for i in range(k):
            maxy = max(hashy, key=hashy.get)
            result.append(maxy)
            del hashy[maxy]

        return result