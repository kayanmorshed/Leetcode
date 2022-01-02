class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        i = n+1
        
        while True:
            strn = str(i)
            
            map_n = {}
            
            for ch in strn:
                if ch not in map_n:
                    map_n[ch] = 1
                else:
                    map_n[ch] += 1
                
            flag = 0
            
            for key in map_n.keys():
                if int(key) != int(map_n[key]):
                    flag = 1
                    break
            
            if flag == 0:
                return i
            else:
                i += 1