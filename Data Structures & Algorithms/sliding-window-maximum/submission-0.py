import heapq
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        result = []
        queue = deque()
        for end in range(len(nums)):
            if (end - start +1) > k:
                # unstable window
                heap = [ -i for i in queue]
                heapq.heapify(heap)
                result.append(-heap[0])

                start +=1
                queue.popleft()

            # stable window, add value
            queue.append(nums[end])
        if queue:
            # for last stable window
            heap = [ -i for i in queue]
            heapq.heapify(heap)
            result.append(-heap[0])
        return result

