class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1: return 5 # 5C1 = 5
        # if n == 2: return 15 # 5C2 + 5C1 = 15
        
        # number of combinations to get with the first caracter 'a', 'e', 'i', 'o', 'u'
        # ways = [5, 4, 3, 2, 1] 
        # latest_length = 15
        
        ways = [1, 1, 1, 1, 1] 
        latest_length = 5
        
        for num in range(2, n+1):
            a = latest_length
            e = latest_length - ways[0]
            i = latest_length - ways[0] - ways[1]
            o = latest_length - ways[0] - ways[1] - ways[2]
            u = latest_length - ways[0] - ways[1] - ways[2] - ways[3]
            
            ways = [a, e, i, o, u]             
            latest_length = a + e + i + o + u
            
        return latest_length
        
        