class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        anagramp_map = {}
        
        for item in strs:
            sort_item_list = sorted(item)
            
            sort_item = ''
            for ch in sort_item_list:
                sort_item += ch 
            
            if sort_item in anagramp_map:
                anagramp_map[sort_item].append(item)
            else:
                anagramp_map[sort_item] = [item]
        
        result = []
        for key in anagramp_map:
            result.append(anagramp_map[key])
        
        return result
                