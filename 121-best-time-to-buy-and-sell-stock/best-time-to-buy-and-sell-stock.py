class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price_seen_so_far = prices[0]
        max_profit = 0
        for price in prices:
            if price < lowest_price_seen_so_far:
                lowest_price_seen_so_far = price
            profit = price - lowest_price_seen_so_far
            if profit > max_profit:
                max_profit = profit
        return max_profit

        