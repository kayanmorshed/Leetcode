class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        output_str = [''] * numRows
        idx, step = 0, 1
        
        for ch in s:
            output_str[idx] += ch
            
            # when row = 0 is touched, set the step = 1
            if idx == 0:
                step = 1
            
            # when row = numRows-1 is touched, step the step = -1 
            # so that the characers can added backwardly
            elif idx == numRows - 1:
                step = -1
            
            # increase the index based on the current step value
            idx += step
        
        return ''.join(output_str)
                