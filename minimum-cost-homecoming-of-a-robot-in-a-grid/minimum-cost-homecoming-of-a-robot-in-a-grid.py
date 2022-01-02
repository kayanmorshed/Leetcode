class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        cost = 0
        
        sr, sc = startPos[0], startPos[1]
        tr, tc = homePos[0], homePos[1]
        
        if sr < tr:
            for i in range(sr + 1, tr+ 1):
                cost += rowCosts[i]
        elif sr > tr:
            for i in range(sr -1, tr - 1, -1):
                cost += rowCosts[i]
        
        if sc < tc:
            for i in range(sc + 1, tc+ 1):
                cost += colCosts[i]
        elif sc > tc:
            for i in range(sc -1, tc - 1, -1):
                cost += colCosts[i]
        
        return cost
        
        
        
        
        
        
#         num_rows, num_cols = len(rowCosts), len(colCosts)
        
#         def dfs (r, c, cost):
#             if r == homePos[0] and c == homePos[1]:
#                 cost += 0
                
#             if r > 0 and homePos[0] < r: 
#                 cost += rowCosts[r-1]
#                 dfs(r-1, c, cost) # top
            
#             if r < num_rows-1 and homePos[0] > r:
#                 cost += rowCosts[r+1]
#                 dfs(r+1, c, cost) # bottom
            
#             if c > 0 and homePos[1] < c:
#                 cost += colCosts[c-1]
#                 dfs(r, c-1, cost) # left
            
#             if c < num_cols-1 and homePos[1] > c:
#                 cost += colCosts[c+1]
#                 dfs(r, c+1, cost) # right
        
#         # call dfs()
#         total = 100000000
#         cost = 0
        
#         for row in range( startPos[0], num_rows):
#             for col in range( startPos[1], num_rows):
#                 if row == homePos[0] and col == homePos[1]:
#                     total = min(total, cost)
#                 else:
#                     cost = 0
#                     dfs(row, col, cost)
        
#         return total