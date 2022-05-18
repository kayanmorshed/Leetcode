# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: 
            return []
        
        return self.createAllBST(1, n)
    
    
    def createAllBST(self, start, end):
        if start > end:
            return [None]
        
        all_trees = []
        
        # create BST considering every integer as root value
        for curr in range(start, end+1):
            
            # get all left subtrees
            left_trees = self.createAllBST(start, curr-1)
            
            # get all right subtrees
            right_trees = self.createAllBST(curr+1, end)
            
            # iterate through left_trees and right_trees to construct possible trees with the root value = curr
            for each_left in left_trees:
                for each_right in right_trees:
                    # generate the root node, left node and right node
                    root = TreeNode(curr)
                    root.left = each_left
                    root.right = each_right
                    
                    # append the newly constructed tree into all_trees[]
                    all_trees.append(root)
        
        return all_trees
                    
            
        
        
        