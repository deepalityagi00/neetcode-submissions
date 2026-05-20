class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        min_target = 2000
        while start <= end:
            mid = (start+end)//2
            min_target = min(nums[mid], min_target)
            
            if nums[start] <= nums[end]:
                min_target = min(min_target, nums[start])
                break

            if nums[start] <= nums[mid]:
                # check if less than target present
                # in sorted array
                if nums[start] <= min_target < nums[mid]:
                    end = mid -1 
                else:
                    start = mid +1
            else:
                if nums[mid] < min_target <= nums[end]:
                    start = mid +1
                else:
                    end = mid -1
        return min_target