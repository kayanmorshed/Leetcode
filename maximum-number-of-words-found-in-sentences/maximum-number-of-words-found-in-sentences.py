class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        
        for item in sentences:
            wlist = item.split(' ')
            
            temp = 0
            for each in wlist:
                if each not in '' or ' ':
                    temp += 1
            
            res = max(res, temp)
        
        return res
                    
        