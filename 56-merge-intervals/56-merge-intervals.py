class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the list "intervals" using the 1st element of each interval
        intervals.sort()
        
        # output list
        merged = []
        
        for interval in intervals:
            # if the merged list is empty and the current interval does not
            # overlap with any of the intervals in merged, simply append it
            
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            
            else:
                # otherwise, there is an overlap
                # so, we merge the current and previous intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged