"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return 
        
        Q = [root] # to hold all nodes of a certain level
        node_list = [] # list to include traversed nodes
        
        while len(Q) > 0:
            curr_nodes = Q
            curr_output_list = []
            Q = []
            
            for node in curr_nodes:
                curr_output_list.append(node.val)
                
                if node.children:
                    for child in node.children:
                        Q.append(child)
            
            node_list.append(curr_output_list)
        
        return node_list
            
        