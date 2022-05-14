class Solution:
    def longestPalindrome(self, s: str) -> str:
        # get the longest palindrome (from inner to outer)
        # left and right are the middle indices, when the length of the string is even
        # left = right = middle index, when the length of the string is odd   

        def getLongestPalidrome(s, left, right): 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]                
        

        # *********** Computation starts here ************
        res = ""
        
        for idx in range(len(s)):
            # call the method getLongestPalidrome() thinking 
            # the current index as middle index
            
            # only one middle index (len(s) = odd)
            returnedPalindrome = getLongestPalidrome(s, idx, idx)  # idx = 1
            if len(returnedPalindrome) > len(res):
                res = returnedPalindrome
            
            # two middle indices
            returnedPalindrome = getLongestPalidrome(s, idx, idx+1)  # idx = 1,2
            if len(returnedPalindrome) > len(res):
                res = returnedPalindrome             

        return res
 

        