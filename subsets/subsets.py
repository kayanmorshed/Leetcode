class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        
        for num in nums:
            curr_set = []
            for item in power_set:
                temp = item.copy()
                temp.append(num)
                curr_set.append(temp)

            for each in curr_set:
                power_set.append(each)
        return power_set
                
            
            
        