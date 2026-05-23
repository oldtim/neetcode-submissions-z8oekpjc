class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(len(dp)-1):
                if dp[j] > 0 and (j+coins[i]) < len(dp):                    
                    dp[j+coins[i]] = dp[j+coins[i]] + dp[j]
        
        return dp[-1]
                



        