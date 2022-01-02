# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        
        def postorder(root):
            left, right = 0, 0

            if root.left: 
                left = postorder(root.left)
                
            if root.right: 
                right = postorder(root.right)
            
            return left + right + 1              
        
        
        # call the method postorder()
        count = postorder(root)
        
        return count
        