"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        
        Q = [root]
        
        while len(Q) > 0:
            temp = []
            while True:
                curr_node = Q.pop(0)
                
                if curr_node.left: temp.append(curr_node.left)
                if curr_node.right: temp.append(curr_node.right)
                
                if len(Q) > 0: 
                    curr_node.next = Q[0]
                else:
                    curr_node.next = None
                    break       
            
            # append the list 'temp' into 'Q'
            Q = temp[:]
         
        return root