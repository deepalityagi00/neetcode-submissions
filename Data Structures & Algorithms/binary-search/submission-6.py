class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end)//2
            current_num = nums[mid]
            if current_num == target:
                return mid
            elif current_num > target:
                #go left - it have smaller numbers 
                end = mid - 1
            else:
                #go right
                start = mid +1 
        return -1
