# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if root.left: inorder(root.left) # for left child
            node_list.append(root.val) # for parent node
            if root.right: inorder(root.right) # for right child       
        
        # call the method inorder()
        node_list = []
        inorder(root)
        
        return node_list[k-1]
        