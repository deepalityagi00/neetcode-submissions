import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(piles,k):
            total_hour = 0
            for banana in piles:
                total_hour += math.ceil(banana/k)
            return total_hour <= h

        start=1
        end = max(piles)
        min_k = max(piles)
        while start<=end:
            mid = (start+end)//2
            if can_finish(piles,mid):
                min_k = min(min_k, mid)
                end = mid -1
            else:
                start = mid +1
        return min_k
            
