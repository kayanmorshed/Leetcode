# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result = '~'
        
        def dfs(node, curr_str):
            if node:
                # get the currect character into the string
                curr_str.append(chr(node.val + ord('a')))
                
                if not node.left and not node.right:
                    # update the reversed result if the current string is 
                    # lexicographically smallest than the result
                    self.result = min(self.result, ''.join(curr_str[::-1]))
                
                dfs(node.left, curr_str)
                dfs(node.right, curr_str)
                
                # remove the last character
                curr_str.pop()
                
        # call the method dfs()
        dfs(root, [])
        
        return self.result
        
        