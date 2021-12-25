class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        while True:
            curr = []
            for item in res:
                for num in nums:
                    if num not in item:
                        curr.append(item + [num])
            res = curr
            
            if len(res[0]) == len(nums):
                break
                    
        return res
        