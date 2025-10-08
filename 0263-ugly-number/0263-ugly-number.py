class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False  # Ugly numbers are positive integers only
    
        for factor in [2, 3, 5]:
            while n % factor == 0:  # Keep dividing by 2, 3, or 5
                n //= factor
        
        return n == 1 