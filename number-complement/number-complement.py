class Solution:
    def findComplement(self, num: int) -> int:
        num_bin_flipped = []
        
        while num > 0:
            remainder = num % 2
            if remainder == 0:
                num_bin_flipped.insert(0, 1)
            else:
                num_bin_flipped.insert(0, 0)
            num = num // 2
            
        output_num = 0
        
        final_idx = len(num_bin_flipped) - 1
        
        for i in range(final_idx, 0, -1):
            if num_bin_flipped[i] == 1:
                output_num += (2 ** (final_idx - i)) 
        
        return output_num
            
        
        