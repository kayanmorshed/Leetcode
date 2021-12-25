class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums = sorted(nums)
        output_list = []
        length = len(nums)
        
        for idx, first_num in enumerate(nums):
            if idx > 0 and first_num == nums[idx -1]: # there is a duplicate
                continue
            
            left_pointer = idx + 1
            right_pointer = length - 1
            
            while left_pointer < right_pointer:
                
                if nums[left_pointer] + nums[right_pointer] + first_num == 0: # triplet found   
                    output_list.append([first_num, nums[left_pointer], nums[right_pointer]]) 
                    left_pointer += 1
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]: # duplicates in nums[left_pointer]
                        left_pointer += 1
                
                elif first_num + nums[left_pointer] + nums[right_pointer] < 0:
                    left_pointer += 1
                
                else:
                    right_pointer -= 1
        
        return output_list
                    
                        