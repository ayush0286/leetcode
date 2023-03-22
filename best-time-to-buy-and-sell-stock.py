class Solution:
    # O(n) Time | O(1) Space, where n is length of prices
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyIndex = 0
        
        for sellIndex in range(1, len(prices)):
            sellPrice = prices[sellIndex]
            buyPrice = prices[buyIndex]

            # profitable transaction
            if sellPrice >= buyPrice:
                profit = sellPrice - buyPrice
                maxProfit = max(maxProfit, profit)
            else:
                buyIndex = sellIndex
        return maxProfit
      
