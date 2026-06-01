import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums[:k]

        heapq.heapify(self.nums)

        # Push the greater elemnts in the heap
        for i in range(k, len(nums)):
            smallest = self.nums[0]
            number = nums[i]
            if smallest < number:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, number)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
            
        return self.nums[0]

