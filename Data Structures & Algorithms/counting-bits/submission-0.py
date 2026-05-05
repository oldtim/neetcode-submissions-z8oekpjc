class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        dp = [0,1]
        for i in range(2, n+1):
            dp.append(dp[i//2] + i%2)
        
        return dp


        
        