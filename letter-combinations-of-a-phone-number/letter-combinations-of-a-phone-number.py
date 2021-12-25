class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        alphabet = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
    
        # to hold the combinations
        comb = ['']
        
        for digit in digits.strip(): # loop through each digit given in the testcase
            current_comb = []
            for letter in alphabet[digit]: # loop through the letter list against each digit
                for combination in comb: # loop through the already formed output combinations
                    current_comb.append(combination + letter)
            
            # replace comb with the current_comb
            comb = current_comb
                
        return comb
        