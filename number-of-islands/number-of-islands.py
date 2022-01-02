class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0
        
        # dfs traversal method
        def dfs_grid_traversal(row, col):
            if grid[row][col] == '1':
                # if '1', make it '-1' to mean that we already visited that cell
                grid[row][col] = '-1'
                
                if row > 0: dfs_grid_traversal(row-1, col) # top
                if row < num_rows-1 : dfs_grid_traversal(row+1, col) # bottom
                if col > 0: dfs_grid_traversal(row, col-1) # left
                if col < num_cols-1 : dfs_grid_traversal(row, col+1) # right
        
        
        # call the dfs_grid_traversal() method starting from [0,0]
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    num_islands += 1
                    dfs_grid_traversal(row, col)
        
        return num_islands