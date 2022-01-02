class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0

        first = 0
        i = 0
        while i < len(bank):
            fmap = Counter(bank[i])
            if '1' in fmap:
                first = fmap['1']
                break
            i += 1

        
        for j in range(i+1, len(bank)):
            smap = Counter(bank[j])
            
            if '1' in smap:
                res += (first * smap['1'])
                first = smap['1']
        
        return res
        
        