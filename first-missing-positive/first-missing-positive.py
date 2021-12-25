class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest_positive = 1
        
        for item in sorted(nums):
            if item <= 0 or item < smallest_positive: 
                continue
            else:
                if item == smallest_positive:
                    smallest_positive += 1
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == smallest_positive: 
                smallest_positive += 1
            # if nums[i] < smallest_positive:
            #     continue
        return smallest_positive
        