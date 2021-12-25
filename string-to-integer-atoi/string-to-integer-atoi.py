class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        
        digit_found = 0
        sign_found = 0
        sign = ''
        num = ''
        
        for ch in s:
            if ch == ' ' and (digit_found == 1 or sign_found == 1): break
            
            if ch == ' ' and digit_found == 0: continue
                        
            if not ch.isdigit() and ch not in '+-':
                break
                
            if ch in '+-' and digit_found == 0 and sign_found == 0: 
                sign = ch
                sign_found = 1
                continue
            
            if ch in '+-' and (sign_found == 1 or digit_found):
                break
            
            if ch.isdigit():
                num += ch
                digit_found = 1

        if len(num) == 0: return 0
        
        if sign == '-':
            num_ = int(num)
            if num_ > (2 ** 31): return (-1) * (2 ** 31)
            else: return (-1) * num_
        
        else:
            num_ = int(num)
            if num_ > (2 ** 31) -1: return (2 ** 31) -1
            else: return num_