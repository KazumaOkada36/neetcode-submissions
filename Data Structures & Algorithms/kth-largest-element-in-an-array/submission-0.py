import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        n = 0
        while n<k:
            a = heapq.heappop_max(nums)
            n += 1
        return a
        