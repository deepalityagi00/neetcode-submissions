import heapq
from math import sqrt, pow
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        priority_queue = []
        for point in points:
            x1 = point[0]
            y1 = point[1]

            dist = sqrt(pow(x1,2) + pow(y1,2))
            heapq.heappush(priority_queue, (dist, point))
        
        result = []
        print(priority_queue)
        for i in range(k):
            _, point = heapq.heappop(priority_queue)
            result.append(point)
        return result
