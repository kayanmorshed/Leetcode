# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # method for preorder traversal
        def preorder(root, row, col):
            
            if col in coord:
                coord[col].append((row, root.val))
            else:
                coord[col] = [(row, root.val)]
            
            if root.left: preorder(root.left, row + 1, col - 1) # for left child
            if root.right: preorder(root.right, row + 1, col + 1) # for left child
        
        
        # call the method preorder()
        coord = {} # dictionary to hold the node values along with row number against the column numbers
        if root: 
            preorder(root, 0, 0)
            
        output = []
            
        for key in sorted(coord.keys()):  
            if len(coord[key]) == 1:
                value = coord[key][0][1]
                output.append([value])
            
            else: # a column has nodes in multple rows
                temp = []
                for item in sorted(coord[key]):
                    temp.append(item[1])
                output.append(temp)
        
        return output
        