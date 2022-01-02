# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # result = []
        
        def dfs (root, temp_sum):
            nonlocal result
            temp_sum = temp_sum * 10 + root.val
            
            if root.left:
                dfs(root.left, temp_sum)
            if root.right:
                dfs(root.right, temp_sum)
                
            if not root.left and not root.right:
                result += temp_sum
        
        # call the recursive method dfs()
        sum_ = 0
        result = 0
        
        if root:
            dfs(root, sum_)
        
        return result
        
        