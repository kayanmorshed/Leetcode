class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        insert_flag = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                insert_flag = True
                break
        
        if insert_flag == False:
            intervals.append(newInterval)
        
        merged = []
        
        for item in intervals:
            if not merged or merged[-1][1] < item[0]:
                merged.append(item)
            else:
                merged[-1][1] = max(merged[-1][1], item[1])
        
        return merged
        
        