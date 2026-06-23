class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}
        def solve(step):
            if step >= len(cost):
                return 0
            if step not in mem:
                step_cost = cost[step]
                result = min(solve(step+1), solve(step+2))
                mem[step] = result+step_cost
            return mem[step]

        return min(solve(0), solve(1))