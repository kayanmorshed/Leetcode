class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:  
        # edge cases
        if nums[-1] < target: return len(nums)
        if nums[0] > target or not nums: return 0
        if len(nums) == 1: return 0
        
        
        mid = int((len(nums)-1)/2)

        if nums[mid] > target:
            return self.searchInsert(nums[0:mid+1], target)
        
        
        elif nums[mid] < target:
            return (mid + 1) + self.searchInsert(nums[mid+1:], target)
        
        else:
            return mid
    
        

        