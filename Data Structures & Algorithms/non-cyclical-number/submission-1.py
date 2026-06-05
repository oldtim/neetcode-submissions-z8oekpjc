class Solution:
    def isHappy(self, n: int) -> bool:
        def sqrt_digit(n):
            temp = 0
            while n:
                temp += (n%10)**2
                n = n//10
            return temp
    
        past_n = set()
        while n not in past_n:
            past_n.add(n)
            n = sqrt_digit(n)
            
            if n == 1:
                return True
        return False
        