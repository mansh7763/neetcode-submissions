class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = 0
        second = 1
        max_profit = 0

        while second < len(prices):
            if prices[first] < prices[second]:
                max_profit = max(max_profit, prices[second]-prices[first])
            else:
                first = second
            second += 1
        return max_profit