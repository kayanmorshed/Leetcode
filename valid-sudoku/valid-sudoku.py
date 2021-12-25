class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_map = {}
            for j in range(9):
                if board[i][j] not in row_map:
                    row_map[board[i][j]] = 1
                elif board[i][j] != '.':
                    return False

        for i in range(9):
            col_map = {}
            for j in range(9):
                if board[j][i] not in col_map:
                    col_map[board[j][i]] = 1
                elif board[j][i] != '.':
                    return False
       
        def check_box_sudoku (row, col, board):
            given_row = row
            given_col = col
            box_map = {}
            while row < given_row + 3:
                while col < given_col + 3:
                    if board[row][col] not in box_map:
                        box_map[board[row][col]] = 1
                    elif board[row][col] != '.':
                        return False
                    col += 1
                col = given_col
                row += 1
            return True

        
        # call check_box_sudoku() method for thr sub-boxes
        i = 0
        while i < 9:
            j = 0
            is_valid = check_box_sudoku (i, j, board)
            
            if is_valid:
                is_valid = check_box_sudoku (i, j+3, board)
            else: return False
            
            if is_valid:
                is_valid = check_box_sudoku (i, j+6, board)
            else: return False
            
            if is_valid:
                i += 3
            else: 
                return False
        
        return is_valid
        
        