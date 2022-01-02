class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_, max_ = min(sorted(nums)), max(sorted(nums))
        
        min_idx, max_idx = -1, -1
        
        for i in range(len(nums)):
            if nums[i] == min_:
                min_idx = i
            elif nums[i] == max_:
                max_idx = i
        
        front = max(min_idx, max_idx) + 1
        rear = len(nums) - min(min_idx, max_idx)
        both = min(min_idx, max_idx) + 1 + len(nums) - max(min_idx, max_idx)
        
        return min(front, rear, both)
        
#         min_dir = 0 # 0 = front, 1 = rear
#         max_dir = 0 # 0 = front, 1 = rear
        
#         if min_idx > len(nums) - 1 - min_idx:
#             min_dir = 1 # rear
        
#         if max_idx > len(nums) - 1 - max_idx:
#             max_dir = 1 # rear
        
#         print(len(nums))
#         print(min_idx)
#         print(max_idx)
#         print(min_dir)
#         print(max_dir)
        
#         if min_dir == 0 and max_dir == 0:
#             return max(min_idx, max_idx) + 1
        
#         elif min_dir == 1 and max_dir == 1:
#             return len(nums) - min(min_idx, max_idx)
        
#         else:
#             return min(min_idx, max_idx) + 1 + len(nums) - max(min_idx, max_idx) 
        