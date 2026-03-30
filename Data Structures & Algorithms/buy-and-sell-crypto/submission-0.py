class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        min_index = 0
        ans = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                min_index = i
            profit = prices[i] - min_price
            if profit > ans:
                ans = profit
        return ans

            

        