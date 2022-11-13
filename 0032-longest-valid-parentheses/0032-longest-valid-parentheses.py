class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # using dynamic programming (credit: pennlio)
        
        # add an extra closing parenthesis in the beginning to handle edge case
        s = ')' + s
        
        # Initialize a list of len(s) memory space to trace the longest valied parentheses ending at s[i]  
        dp = [0 for x in range(len(s))] # dp[i] = longestValidParentheses ending at s[i]
        mx = 0 # variable to hold the (max) length of the longestValidParentheses so far 
        
        for i in range(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(': 
                    dp[i] = dp[i-2] + 2 # add nearest parentheses pairs + 2
                
                # case 2: (()) 
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid 
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                mx = max(mx, dp[i])
        return mx