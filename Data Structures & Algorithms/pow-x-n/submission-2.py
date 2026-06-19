class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if abs(n) == 1:
            return (x if n > 0 else 1/x) 
        #curr = self.myPow(x, n//2) #錯誤:n//2對負數來說是向下取整數，比如-3//2 = -2
        if n > 0:
            curr = self.myPow(x, n//2)
        else:
            curr = self.myPow(x, (n+1)//2)
            
        if n%2 != 0:
            return (curr*curr*x if n > 0 else curr*curr*(1/x))
        else:
            return curr*curr
        