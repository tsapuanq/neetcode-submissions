class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                n = prices[i] - prices[j]
                if n < max:
                    max = n
        return abs(max)

