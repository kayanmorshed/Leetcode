class Solution:
    def isNumber(self, s: str) -> bool:
        if s[0] in 'eE': return False
        if len(s) == 1: return s[0].isdigit()
            
        digit_found = False
        dot_found = False
        dot_pos = -1
        exp_found = False
        exp_found_check = False
        exp_pos = -1
        sign_found = False
        sign_pos = -1
        isValid = True
        
        for i in range(len(s)):
            if s[len(s)-1] in 'eE' or (not s[i].isdigit() and s[i] not in 'eE' and s[i] not in '+-' and s[i] != '.'):
                return False
            
            # after exponentiation
            if exp_found_check == True:
                sign_found = False
                digit_found = False
                dot_found = False
                exp_found_check = False
            
            if dot_found == True and s[i] == '.': return False
            if dot_found == True and digit_found == False and s[i] in '+-eE' and i == dot_pos + 1: return False
            if dot_found == True and s[i] == '.': return False
            if sign_found == True and s[i] in '-+': return False
            if sign_found == True and s[i] in 'eE' and i == sign_pos + 1: return False
            if (exp_found == True and s[i] in 'eE'): return False
            if (exp_found == True and s[i] == '.'): return False
            if (exp_found == True and (s[i] in '+-' and i != exp_pos + 1)): return False
            if digit_found == True and exp_found == False and s[i] in '+-': return False
            if s[i] not in 'eE' and s[i].isalpha(): return False
            
            if s[i] == '.':
                dot_found = True
                dot_pos = i
                continue
                
            if s[i] == '-' or s[i] == '+':
                sign_found = True
                sign_pos = i
                continue
                
            if s[i].isdigit():
                digit_found = True
                continue
                
            if s[i] in 'eE':
                exp_found = True
                exp_found_check = True
                exp_pos = i
                continue
                    
        return digit_found