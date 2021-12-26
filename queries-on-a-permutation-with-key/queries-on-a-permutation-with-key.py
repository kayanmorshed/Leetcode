class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = []
        res = []
        for i in range(1, m+1): 
            P.append(i)
        
        for item in queries:
            idx = P.index(item)
            res.append(idx)
            P.pop(idx)
            P.insert(0, item)
        
        return res
            
        