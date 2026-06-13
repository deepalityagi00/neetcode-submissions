from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        dirs = [(-1,0),(1,0), (0,-1),(0,1)]

        fresh = 0
        minutes=0
        queue = deque()
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1
        
        if fresh == 0:
            return 0 
        
        while queue and fresh > 0:
                is_rot = False
                for _ in range(len(queue)):
                    fr, fc = queue.popleft()
                    for r, c in dirs:
                        k = fr+r
                        l = fc+c
                        if k < 0 or k>=rl or l < 0 or l >=cl:
                            continue
                        if grid[k][l] == 1:
                            fresh -=1
                            grid[k][l] = 2
                            queue.append((k, l))
                minutes +=1                

        return minutes if fresh == 0 else -1 
        