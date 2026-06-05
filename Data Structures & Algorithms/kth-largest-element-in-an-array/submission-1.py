import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k,len(nums)):
            element = heap[0]
            if element < nums[i]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])

        return heap[0]

