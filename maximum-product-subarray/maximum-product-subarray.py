class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = nums[0] # to contain the "running current product"
        largest = nums[0] # to contain the largest product
        
        for i in range(1, len(nums)):
            curr = 1 # temporary largest product
            
            if nums[i] == 0: # means there is a discontinuation in the subarray
                curr = 0
            
            elif nums[i-1] == 0: # check whether this is the new element of a new subarray
                curr = nums[i]
            
            else:
                curr = max(prod * nums[i], nums[i-1] * nums[i], nums[i])
                nums[i] = min(prod * nums[i], nums[i-1] * nums[i], nums[i])
            
            # replace the existing "running current product" with the "temporary largest product"
            prod = curr
                
            if curr > largest:
                largest = curr
        
        return largest
        