class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        result = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check overflow
            if result > (INT_MAX - pop) // 10:
                return 0
            
            result = result * 10 + pop
        
        return sign * result
