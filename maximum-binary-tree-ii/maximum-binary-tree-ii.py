# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def inorderTraversal(root, node_list):
            if root.left: inorderTraversal(root.left, node_list)
            node_list.append(root.val)
            if root.right: inorderTraversal(root.right, node_list)
        
        # call inorderTraversal(root)
        node_list = []
        inorderTraversal(root, node_list)
        node_list.append(val)
        
        def constructTree(nodes):
            if len(nodes) > 0:
                idx = nodes.index(max(nodes))
                return TreeNode(max(nodes), constructTree(nodes[:idx]), constructTree(nodes[idx+1:]))
        
        return constructTree(node_list)
            
        