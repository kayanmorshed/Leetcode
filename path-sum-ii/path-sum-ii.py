# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(root, target, trace_list):
            # if not root:
            #     return
            
            trace_list.append(root.val)
            
            if not root.left and not root.right and root.val == target:
                result.append(list(trace_list))
                        
            if root.left:
                dfs(root.left, target - root.val, trace_list)
            
            if root.right:
                dfs(root.right, target - root.val, trace_list)
    
            trace_list.pop()
            
        
        # call the method dfs()
        result = []
        if root:
            dfs(root, targetSum, [])
        
        return result
        