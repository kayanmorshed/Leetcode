class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:  
        left, right = -1, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if mid < 0: return 0
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
    
        return right

        