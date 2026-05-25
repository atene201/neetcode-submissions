class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # compare the prev value to current one
        # if the curr value > prev then you can make a profit
        # if the curr value < prev then you cannot make a profit

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit