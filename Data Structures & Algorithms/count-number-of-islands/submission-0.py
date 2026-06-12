class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        def sink(row, col):
            if row<0 or row >= row_len or col<0 or col>=col_len:
                return 
            if grid[row][col] != "1":
                return 
            
            grid[row][col] = "#"
            for l, r in directions:
                sink(row+l,col+r)

        count = 0
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == "1":
                    count +=1
                    sink(row, col)
        return count