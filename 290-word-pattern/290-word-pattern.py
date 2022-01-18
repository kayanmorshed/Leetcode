class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pmap = {}
        smap = {}
        curr_word = ''
        i = 0
        
        for ch in s:
            if ch == ' ':
                if pattern[i] in pmap and pmap[pattern[i]] != curr_word:
                        return False
                
                if curr_word in smap and smap[curr_word] != pattern[i]:
                        return False
                
                pmap[pattern[i]] = curr_word
                smap[curr_word] = pattern[i]
                
                # increase the index for pattern and reset curr_word
                curr_word = ''
                i += 1
                
            else:
                curr_word += ch  
        
        print(i)
        print(curr_word)
        
        if i != len(pattern)-1:
            return False
        
        if pattern[i] in pmap and pmap[pattern[i]] != curr_word:
            return False
        
        if curr_word in smap and smap[curr_word] != pattern[i]:
                        return False
        
        return True
                
                
        
        
        