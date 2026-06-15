class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        if amount == 0:
            return 0

        def solve(am):
            if am < 0:
                return -1
            if am == 0:
                return 0
            if am in mem:
                return mem[am]
            else:

                mini = float('inf')
                for coin in coins:
                    if solve(am-coin) >= 0:
                        mini = min(mini, 1+ solve(am-coin))
                mem[am]=mini if mini != float("inf") else -1
            return mem[am]

        re = solve(amount)
        return re