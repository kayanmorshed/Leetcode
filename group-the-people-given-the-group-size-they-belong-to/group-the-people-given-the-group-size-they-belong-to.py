class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output = []
        dict_ = {}
        
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dict_:
                dict_[groupSizes[i]] = [i]
            else:
                dict_[groupSizes[i]].append(i)
        
        for key in dict_:
            curr = dict_[key]
            
            start = 0
            end = key
            
            while end <= len(curr):
                output.append(curr[start:end])
                start = end
                end += key
    
        
        return output
        