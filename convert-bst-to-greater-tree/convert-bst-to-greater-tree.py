# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        if not root.left and not root.right: return root
        
        def recursive_call(root):
            if root:
                if root.right: recursive_call(root.right)
                node_list.append(root)
                if root.left: recursive_call(root.left)  
        
        # call the method recursive_call() to list all the nodes in the desired order
        node_list = []
        recursive_call(root)
        
        curr_sum = node_list[0].val
        
        for i in range(1, len(node_list)):
            node_list[i].val = curr_sum + node_list[i].val
            curr_sum = node_list[i].val
        
        return root
                
                
            
        