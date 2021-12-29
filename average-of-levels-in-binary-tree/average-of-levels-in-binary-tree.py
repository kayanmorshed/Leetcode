# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        Q = [root]
        res = []
        
        while len(Q) > 0:
            curr_nodes = Q
            next_nodes = []
            
            sum_, count = 0, 0
            for node in curr_nodes:
                sum_ += node.val
                count += 1
                
                # update the child nodes into the list next_nodes
                if node.left: next_nodes.append(node.left)
                if node.right: next_nodes.append(node.right)
                    
            avg_ = sum_/count # make sure it contains value upto 5 decimal point
            res.append(avg_) # update the resultant avg list
            
            Q = next_nodes # update the queue with the next nodes
        
        return res
            
                
        