class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary(nums, target):
            start = 0
            end = len(nums) -1 

            while start<=end:
                mid = (start+end)//2
                if target == nums[mid]:
                    return True
                elif target < nums[mid]:
                    end = mid -1
                else:
                    start = mid +1
            return False 
        
        for row in matrix:
            # check if target may exists in this row 
            if row[0] <= target <= row[-1]:
                return binary(row, target)
        return False