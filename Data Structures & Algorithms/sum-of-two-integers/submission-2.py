class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF 
        max_int = 0x7FFFFFFF

        curr = a ^ b
        carry = (a & b) << 1
        while carry:
            temp_curr = curr ^ carry
            temp_carry = (curr & carry) << 1
            curr = (temp_curr) & mask
            carry = (temp_carry) & mask
        
        return curr if curr <= max_int else ~(curr^mask)