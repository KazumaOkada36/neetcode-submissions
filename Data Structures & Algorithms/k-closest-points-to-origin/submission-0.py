import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        bruh = []
        for point in points:
            distance = (point[0]**2)+(point[1]**2)
            if len(bruh) < k:
                heapq.heappush_max(bruh, (distance, point))
            else:
                distancey = bruh[0][0]
                if distance < distancey:
                    heapq.heappop_max(bruh)
                    heapq.heappush_max(bruh, (distance, point))

        return [item[1] for item in bruh]
                    
                


        