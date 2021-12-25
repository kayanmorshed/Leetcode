# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ***************** from Neetcode tutorial ************
        def recursive_validation(node, left, right):
            if not node:
                return True
            
            if not (left < node.val and right > node.val):
                return False
            
            left_subtree = recursive_validation(node.left, left, node.val)
            right_subtree = recursive_validation(node.right, node.val, right)
            
            return left_subtree and right_subtree 
        
        
        # call the method recursive_validation()
        return recursive_validation(root, float("-inf"), float("inf"))
        
        