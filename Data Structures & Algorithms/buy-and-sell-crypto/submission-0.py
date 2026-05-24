class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = 0
        last = len(prices)-1
        max_profit = 0
        while first <= last:
            max_profit = max(max_profit, prices[last]-prices[first])
            if prices[first+1]<=prices[first]:
                first += 1
            if prices[last-1] >= prices[last]:
                last -= 1
            else:
                first += 1
        return max_profit