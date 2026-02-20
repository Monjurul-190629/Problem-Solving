class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        chosen_price = prices[0]
        profit = 0
        for i in prices[1:]:
            if i < chosen_price:
               chosen_price = i
            else:
               profit = max(profit, i - chosen_price)
        return profit
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4, 11]))