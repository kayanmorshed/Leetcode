class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for idx in range(len(s)):
            # odd case, like "aba"
            tmp = self.getLongestPalidrome(s, idx, idx)
            if len(tmp) > len(res):
                res = tmp
                
            # even case, like "abba"; index = 0,2,4,6
            tmp = self.getLongestPalidrome(s, idx, idx+1)
            if len(tmp) > len(res):
                res = tmp
        return res
 
    # get the longest palindrome (from inner to outer)
    # left and right are the middle indices, when the length of the string is even
    # left = right = middle index, when the length of the string is odd   
    
    def getLongestPalidrome(self, s, left, right): 
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]                
        