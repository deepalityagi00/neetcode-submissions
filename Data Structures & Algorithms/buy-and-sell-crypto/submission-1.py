class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_before = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_before = min(min_before, price)
            max_profit = max(max_profit, price - min_before)
        
        return max_profit