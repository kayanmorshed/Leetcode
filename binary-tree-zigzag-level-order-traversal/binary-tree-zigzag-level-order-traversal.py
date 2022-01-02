# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        if not root.left and not root.right: return [[root.val]]
        
        dir_ = 'left'
        res = []
        Q = [root]
        
        while len(Q) > 0:
            curr_level = Q
            temp_res = []
            next_items = []
            
            if dir_ == 'left':
                for item in curr_level: # traverse from left to right
                    temp_res.append(item.val)
                    if item.left: next_items.append(item.left)
                    if item.right: next_items.append(item.right)
                dir_ = 'right'
                Q = next_items[::-1] # add child from right to left
                res.append(temp_res) # add in the result in the original traversal order
                continue
            
            else:
                for item in curr_level[::-1]: # traverse from right to left
                    temp_res.append(item.val)
                    if item.left: next_items.append(item.left)
                    if item.right: next_items.append(item.right)
                dir_ = 'left'    
            
                Q = next_items # add child from right to left
                res.append(temp_res[::-1]) # output from left to right

        return res
                    
        