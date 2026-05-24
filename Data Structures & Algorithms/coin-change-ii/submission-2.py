class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        #coins.sort() # *必要sort
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):   
            for a in range(amount + 1):
                dp[i][a] = dp[i + 1][a]
                if a >= coins[i]:
                    #dp[i][a] = dp[i + 1][a] # 因為直接繼承>(i+1)th coins的累積可能組合，所以coin[i+1]必須>=coin[i]，所以*必要sort
                    dp[i][a] += dp[i][a - coins[i]] # 再加上

        return dp[0][amount]       
        
        # 解答用2D DP，雖然第一次花了些時間就想出壓縮後1D DP，但為了完整思路，學一下壓縮前的2D
        