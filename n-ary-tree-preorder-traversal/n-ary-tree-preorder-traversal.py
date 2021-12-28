"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def preorder(root):
            if root:
                node_list.append(root.val)
                
                for child_node in root.children:
                    preorder(child_node)
                    
        # call the method preorder() with the "root" node as argument        
        node_list = []
        preorder(root)
        
        return node_list