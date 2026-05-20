class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        note = {}

        for indx, value in enumerate(nums):
            partner = target - value
            if partner in note:
                return [ note[partner], indx]
            else:
                note[value]=indx
