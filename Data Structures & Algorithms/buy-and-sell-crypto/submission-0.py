class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices):
                if prices[i] < prices[j]:
                    value = prices[j] - prices[i]
                    if profit < value:
                        profit = value
                j += 1

        return profit