class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        jump_range = 0 # where we can jump into
        curr = 0 # current index
        
        while curr < len(nums)-1:
            jump_range = max(jump_range, curr + nums[curr])
            
            j = jump_range
            while j > curr:
                if j >= len(nums)-1:
                    return True
                
                jump_range = max(jump_range, j + nums[j])
                j -= 1
                
                if jump_range >= len(nums)-1:
                    return True
            
            if jump_range == curr + nums[curr]:
                return False
            
            # next iteration starts here
            curr = curr + nums[curr] + 1
        
        return False
        
            
            
        
        
        
        