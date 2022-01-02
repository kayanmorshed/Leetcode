class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = len(prices)
        size = 1
        
        for i in range(len(prices)-1):
            if prices[i] - prices[i+1] == 1:
                size += 1
                res += (size - 1)
            else:
                size = 1
        
        return res
        
        
        
        