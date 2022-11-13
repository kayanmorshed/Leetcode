class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # using dynamic programming (credit: pennlio)
        
        # Initialize a list of len(s) memory space to trace the longest valid parentheses ending at s[i]
        dp_length = [0] * len(s)  # dp_length[i] = length of the longest valid parenthesis string ending at s[i]

        mx = 0  # variable to hold the (max) length of the longest valid parenthesis string so far

        # start from index "1" because the input_string[0] alone cannot form a valid parenthesis string
        for i in range(1, len(s)):
            # we are only interested in the closing parenthesis since an opening parenthesis can never complete
            # the formation of a valid string i.e., a ')' dictates the update of dp_length[i]

            if s[i] == ')':
                # ***********************************************************************************
                # case 1: ()()() => opening and closing parentheses exist in every alternate position
                # ***********************************************************************************

                if s[i-1] == '(':
                    # the length of the nearest valid parenthesis string + 2
                    dp_length[i] = dp_length[i-2] + 2

                # *******************************************************************************************
                # case 2: ((())) => a series of opening parenthesis and again a series of closing parenthesis
                # *******************************************************************************************

                # dp_length[i-1] = the length of the nearest valid parenthesis string
                # (i - dp_length[i-1]) - 1 = the index of last "(" not paired until the current ")"

                elif (i - dp_length[i-1]) - 1 >= 0 and s[i - dp_length[i-1] - 1] == '(':
                    # check whether the length of the nearest valid parenthesis string is > 0
                    if dp_length[i-1] > 0:
                        # length of the nearest valid parenthesis string + 2
                        # + length of the valid parenthesis string before last unpaired "("
                        dp_length[i] = dp_length[i-1] + 2 + dp_length[i - dp_length[i-1] - 2]
                    else:
                        dp_length[i] = 0 # no consecutive matching '(' and ')'

                # update the length of the longest valid parenthesis string so far
                mx = max(mx, dp_length[i])
        
        return mx