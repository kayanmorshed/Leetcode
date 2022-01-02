# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == p or root == q or root == None:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # left subtree returns NULL, so return any NULL/Non-NULL value in right
        if not left: 
            return right 
        
        # right subtree returns NULL, so return any NULL/Non-NULL value in left
        elif not right: 
            return left
        
        # both left and right return non-NULL values
        else: 
            return root 