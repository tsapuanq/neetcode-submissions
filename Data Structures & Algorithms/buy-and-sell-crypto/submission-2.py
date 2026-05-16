class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                diff = prices[j] - prices[i]
                if diff > max_diff:
                    max_diff = diff
        return max_diff

