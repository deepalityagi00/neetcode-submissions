class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_num = set(nums)
        max_length = 0
        for num in nums:
            if num-1 in my_num:
                continue
            i = num
            len = 0
            while i in my_num:
                len +=1
                max_length = max(max_length, len)
                i +=1
        return max_length