class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0;

        # main loop move right
        # run a second loop 

        for right in range(len(prices)):
            inner = right
            while inner < len(prices):
                if prices[inner] > prices[left]:
                    total = prices[inner] - prices[left]
                    if total > profit:
                        profit = total
                inner +=1
            left += 1
        return profit