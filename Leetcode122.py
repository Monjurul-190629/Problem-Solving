class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        chosen_price = prices[0]
        for i in range(1, len(prices)):
            