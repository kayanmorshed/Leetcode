class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pleft, pleft_pos = [], []
        toDel = []
        
        for idx, ch in enumerate(s):
            if ch == '(':
                pleft.append('(')
                pleft_pos.append(idx)

            elif ch == ')':
                if len(pleft) == 0:
                    toDel.append(idx)
                    continue
                else:
                    pleft.pop(0)
                    pleft_pos.pop(0) 
            
        result = ''
        
        for idx, ch in enumerate(s):
            if idx in pleft_pos or idx in toDel:
                continue
            result += ch
        
        return result
                        
                    
                
        