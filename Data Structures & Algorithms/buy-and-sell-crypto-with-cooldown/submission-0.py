class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [len(prices)*[-1] for _ in range(len(prices))]
        for buy in range(len(prices)):
            temp = -1
            for sell in range(buy+1, len(prices)):
                temp = max(temp, prices[sell] - prices[buy])
                dp[buy][sell] = temp
        
        ans_max = 0

        for buy in range(1, len(prices)):     #從1開始
            for sell in range(buy, len(prices)):
                previous_remain = dp[buy-1][sell]
                if buy - 2 >= 0 and dp[buy-2][buy-2] > 0:
                    newone_add = dp[buy-2][buy-2] + dp[buy][sell]
                else:
                    newone_add = dp[buy][sell]
                dp[buy][sell] = max(previous_remain, newone_add)
                ans_max = max(ans_max, dp[buy][sell])
        
        return ans_max
                


        