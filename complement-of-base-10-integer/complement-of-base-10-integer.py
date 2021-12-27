class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        complement = []
        
        while n > 0:
            remainder = n % 2
            if remainder == 0:
                complement.insert(0, 1)
            else:
                complement.insert(0, 0)
            n = n // 2
            
        output_num = 0
        final_idx = len(complement) - 1
        
        for i in range(final_idx, 0, -1):
            if complement[i] == 1:
                output_num += (2 ** (final_idx - i)) 
        
        return output_num

        