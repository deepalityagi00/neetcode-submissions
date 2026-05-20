class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) -1 
        max_water = 0
        while start < end:
            width = end-start
            current_trap = width*min(heights[end],heights[start])
            max_water = max(current_trap,max_water )
            if heights[end] < heights[start]:
                end -=1
            else:
                start +=1
        
        return max_water