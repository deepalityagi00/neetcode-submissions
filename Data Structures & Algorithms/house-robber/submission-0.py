class Solution:
    def rob(self, nums: List[int]) -> int:
        
        last_house = len(nums) - 1
        mem = {}
        def solve(house_num):
            if house_num < 0:
                return 0
            if house_num in mem:
                return mem[house_num]
            rob = nums[house_num] + solve(house_num-2)
            skip = solve(house_num-1)
            mem[house_num] = max(skip, rob)
            return mem[house_num]
        
        return solve(last_house)