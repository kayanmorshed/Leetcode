class Solution:
    def numTrees(self, n: int) -> int:
        '''
        num_nodes       num_tree
            0               1
            1               1
            2               2
            3               5
            4               14
        
                        left           right
        num_tree(4) = num_tree(0) * num_tree(3) # when root = 0
                      num_tree(1) * num_tree(2) # when root = 1
                      num_tree(2) * num_tree(1) # when root = 2
                      num_tree(3) * num_tree(0) # when root = 3
        '''
        
        num_tree = [0] * (n + 1) # num_tree = [0, 0, .........., (n+1) times]
        num_tree[0] = 1 # for n = 0; empty tree 
        
        for num in range(1, n+1):
            for rest in range(0, num):
                left =  rest
                right = (num - 1) - rest
                
                num_tree[num] += num_tree[left] * num_tree[right]
        
        return num_tree[n]
        