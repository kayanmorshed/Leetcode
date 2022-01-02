class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        if len(asteroids) == 1:
            return (mass >= asteroids[0])
        
        curr = mass
        sort_ast = sorted(asteroids)

        for i in range(len(sort_ast)-1):
            curr += sort_ast[i]
            if curr < sort_ast[i+1]:
                return False
        
        return True
            
        