import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weight = list(map(lambda x: -x, stones))
        heapq.heapify(weight)

        while len(weight) >= 2:
            stone1 = - heapq.heappop(weight)
            stone2 = - heapq.heappop(weight)

            if stone1 < stone2:
                new_stone = stone2 - stone1
                heapq.heappush(weight, -new_stone)
            elif stone1 > stone2:
                new_stone = stone1 - stone2
                heapq.heappush(weight, -new_stone)
        
        if len(weight) == 1:
            return - weight[0]
        else:
            return 0
