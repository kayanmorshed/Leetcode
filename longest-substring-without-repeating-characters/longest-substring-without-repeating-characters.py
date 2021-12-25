class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        longest = 1
        i = 1
        curr = s[0]
        while i < len(s):
            if s[i] in curr:
                longest = max(longest, len(curr))
                idx = curr.find(s[i])
                curr = curr[idx+1:i+1] + s[i]
            else:
                curr += s[i]
            i += 1
            
        if len(curr) > longest:
            return len(curr)
        
        return longest

            
        