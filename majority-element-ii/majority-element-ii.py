class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums)//3
        
        element = {}
        res = []
        
        for num in nums:
            if num not in res:
                if num in element:
                    element[num] += 1
                else:
                    element[num] = 1
            
                if element[num] > threshold:
                    res.append(num)        
        return res