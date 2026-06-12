class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        def sink(r, c):
            if r<0 or r>=row_len or c<0 or c>=col_len:
                return 0
            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = "#"
            area = 1
            for dr, dc in [(0,-1), (0,1), (-1,0), (1,0)]:
                area +=sink(r+dr, c+dc)
            return area 

        max_area = 0

        for rw in range(row_len):
            for cl in range(col_len):
                if grid[rw][cl] == 1:
                    max_area = max(max_area, sink(rw, cl))
        
        return max_area

        
