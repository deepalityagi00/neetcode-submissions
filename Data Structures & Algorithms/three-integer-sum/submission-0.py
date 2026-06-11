class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a+b = -c 
        nums = sorted(nums)
        result = set()
        for idx, num in enumerate(nums):
            start = idx +1
            end = len(nums)-1
            #[-4,-1,-1,0,1,2]
            while start < end:
                # 1 =! 4
                current_sum = nums[start] + nums[end]
                if current_sum == - num:
                    result.add((nums[start], nums[end], num))
                    start +=1
                    end -=1
                elif current_sum < -num:
                    start +=1
                else:
                    end -=1
        return list(result)