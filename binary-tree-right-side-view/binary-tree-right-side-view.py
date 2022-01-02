# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return
        
        right_side = []
        
        def dfs(node, level):
            if level == len(right_side):
                right_side.append(node.val)
            
            for child in [node.right, node.left]:
                if child:
                    dfs(child, level + 1)        
        
        
        # call the method dfs() with level = 0 at the root node
        level = 0
        dfs(root, level)
        
        return right_side
        