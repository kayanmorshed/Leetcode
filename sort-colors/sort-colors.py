class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method to partition a given array using two pointer
        def partition(nums, start, end):
            pivot = nums[end]
            i = start-1
            
            for j in range(start, end):
                if nums[j] <= pivot:
                    i += 1        
                    # exchange between nums[i] and nums[j]
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
            
            # exchange between nums[i+1] and nums[end]
            temp = nums[i+1]
            nums[i+1] = nums[end]
            nums[end] = temp
            return i+1
    
        # method to perform quickSort() operation
        def quickSort(nums, start, end):
            if start < end:
                mid = partition(nums, start, end)
                quickSort(nums, start, mid-1)
                quickSort(nums, mid+1, end)
        
        # call the method quickSort() to sort by colors
        start, end = 0, len(nums)-1
        quickSort(nums, start, end)
        