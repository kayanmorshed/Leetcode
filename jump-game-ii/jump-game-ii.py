class Solution:
    def jump(self, nums: List[int]) -> int:
        # create a list to track how many jumps have been made to reach current index
        import math
        jump = [math.inf]*len(nums)
        
        jump[0] = 0 # no jump required to reach index 0
        pivot = 0
        
        for i in range(0, len(nums)-1):
            j = nums[i] # integer of index i
            while i+j > i:
                if (i+j) <= len(nums)-1:
                    jump[i+j] = min(jump[i+j], jump[i]+1)
                else:
                    diff = (i+j) - (len(nums)-1)
                    j -= diff-1
                j -= 1
            
        return jump[-1]