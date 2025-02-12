class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        negative = (dividend < 0) ^ (divisor < 0) 
        
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = dividend // divisor
        if negative:
            quotient = -quotient
        
        return max(-2**31, min(quotient, 2**31 - 1))  
