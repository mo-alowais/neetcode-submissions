class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, v in enumerate(prices[::-1]):
            for j in prices[::-1][i:]:
                if v - j > profit: profit = v - j
        return profit
        