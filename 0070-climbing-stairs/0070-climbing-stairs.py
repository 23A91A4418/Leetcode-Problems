class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n  # base cases: 1 way for 1 step, 2 ways for 2 steps
    
        first, second = 1, 2  # first = ways to reach step 1, second = ways to reach step 2
        for i in range(3, n + 1):
            third = first + second  # ways to reach current step
            first, second = second, third  # update for next iteration
        
        return second