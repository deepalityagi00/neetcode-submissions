class Solution:
    def climbStairs(self, n: int) -> int:
        step_cal = {}
        def solve(step):
            if step == 0:
                return 1
            if step < 0:
                return 0 
            if step in step_cal:
                result = step_cal.get(step)
            else:
                result = solve(step-1) + solve(step-2)
                step_cal[step] = result
            return result
        return solve(n)