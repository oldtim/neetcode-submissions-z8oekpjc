class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        ans = 1
        for _ in range(abs(n)):
            ans = ans*x
        
        if n < 0 :
            ans = 1/ans
        
        return ans


        