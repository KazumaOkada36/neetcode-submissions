import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = nums
        heapq.heapify(nums)
        while len(self.queue) > self.k:
            heapq.heappop(self.queue)


    def add(self, val: int) -> int:
        if len(self.queue) == self.k:
            if val > self.queue[0]:
                heapq.heappop(self.queue)
                heapq.heappush(self.queue, val)
                return self.queue[0]
        elif len(self.queue) < self.k:
            heapq.heappush(self.queue, val)
        return self.queue[0]


        
