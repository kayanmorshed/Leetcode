# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def preorder(root):
            sum_ = 0
            if root:
                if root.val >= low and root.val <= high:
                    sum_ += root.val
                if root.left: 
                    sum_ += preorder(root.left)
                if root.right: 
                    sum_ += preorder(root.right)
            return sum_
                
        # call the method preorder
        sum_ = preorder(root)
        
        return sum_
        