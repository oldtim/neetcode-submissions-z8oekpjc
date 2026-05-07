class Solution:
    def reverseBits(self, n: int) -> int:
        new_n = 0
        for i in range(32):
            new_n = new_n + (n % 2)*(2**(31-i))
            n = n // 2
        
        return new_n


        