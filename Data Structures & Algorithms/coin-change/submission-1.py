class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #coins.sort()  # 因為coins最多只有10種，logN << t (最高10000)

        dp = [-1]*(amount+1) #
        dp[0] = 0
        for i in range(len(dp)):
            for j in range(len(coins)):
                if dp[i] >= 0 and (i + coins[j]) <= amount:
                    if dp[(i + coins[j])] < 0:
                        dp[(i + coins[j])] = dp[i] + 1
                    else:
                        dp[(i + coins[j])] = min(dp[(i + coins[j])], dp[i]+1)
        
        return dp[-1]

        #瞄一眼解答: 轉換思路，因為coins是整數，可把每一點amount當作dp格子，每格紀錄累積到此量所需最小次數