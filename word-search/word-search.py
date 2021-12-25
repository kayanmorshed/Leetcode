class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        num_rows, num_cols = len(board), len(board[0])
        
        # dfs() definition
        def dfs(row, col, board, idx, word):  
            char = board[row][col]
            
            if char == word[idx]:
                if idx == len(word)-1:
                    return True
            else:
                return False
            
            # replace the character in the current position with NULL
            board[row][col] = None
                            
            if row > 0 and dfs(row-1, col, board, idx+1, word):
                return True
            
            if row < num_rows-1 and dfs(row+1, col, board, idx+1, word):
                return True
            
            if col > 0 and dfs(row, col-1, board, idx+1, word):
                return True
            
            if col < num_cols-1 and dfs(row, col+1, board, idx+1, word):
                return True
                        
            # replace the original character in the board
            board[row][col] = char                  
            return False
        
        # check whether there are more characters in "word" than the board
        if len(word) > num_rows * num_cols:
            return False
    
        
        # dfs() calling
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col]== word[0]:
                    idx = 0 # idx of the charcater in word we are interested in
                    found = dfs(row, col, board, idx, word)
                if found == True:
                    return True
                    
        return found
        
        