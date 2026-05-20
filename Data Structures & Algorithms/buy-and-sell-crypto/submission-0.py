class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for index in range(1,len(prices)):
            
            max_profit = max(
                prices[index] - buy, 
                max_profit)
            buy = min(buy,prices[index])
        return max_profit
            