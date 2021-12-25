class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            curr_set = []
            
            for item in res:
                curr = item.copy()
                curr_set.append(curr + [num])
            
            for each in curr_set:
                if sorted(each) not in res:
                    res.append(sorted(each))
        
        return res