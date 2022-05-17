class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = {}
        
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        res = 0
            
        for key in freq.keys():
            val = freq[key]
            
            if val == 1:
                return -1
            
            res += (val + 2) // 3
        
        return res
        
        