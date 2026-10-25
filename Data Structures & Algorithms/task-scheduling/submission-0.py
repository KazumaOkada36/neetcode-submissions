from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashy = {}
        for letter in tasks:
            if letter in hashy:
                hashy[letter] += 1
            else:
                hashy[letter] = 1
        heap = []
        for item in hashy.values():
            heapq.heappush_max(heap, item)
        
        count = 0
        queue = deque()
        while heap or queue:
            if heap:
                yay = heapq.heappop_max(heap)
                if yay>1:
                    queue.append((yay-1, count+n))
            if queue and queue[0][1] <= count:
                g = queue.popleft()
                heapq.heappush_max(heap, g[0])                          

            count += 1
        
        return count

        
        
        