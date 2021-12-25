class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursive_mypow(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            result = recursive_mypow(x, n//2)
            result = result * result
            
            if n% 2 == 1:
                return x * result
            else:
                return result
        
        # call recursive_mypow() method
        final_result = recursive_mypow(x, abs(n))
        
        if n >= 0:
            return final_result
        else:
            return 1 / final_result
            