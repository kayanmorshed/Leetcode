class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        steps: n
        steps each time: 1 or 2
        obj: number of distinct ways to reach the top
        
        n = 1: 1 way
        n = 2: 1 + 1, 2 = 2 ways
        n = 3: 1 + 1 + 1, 1 + 2, 2 + 1 = 3 ways
        n - 4, 1 + 1 + 1 + 1, 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1, 2 + 2 = 5 ways 
        
        '''
        
        if n == 1 or n == 2:
            return n
        
        first, second = 1, 2
        
        i = 3
        while i <= n:
            first, second = second, first + second
            i += 1
        
        return second
            
        