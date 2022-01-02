class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        length = len(arr)
        self.cmap = collections.defaultdict(list)
        
        for idx, val in enumerate(arr):
            self.cmap[val] += [idx]

    def query(self, left: int, right: int, value: int) -> int:
        # to get the position of 'left' into the list cmap[value]
        # if 'left' exists on the list, then the left index of the first occurence will be returned
        idx_left = bisect.bisect_left(self.cmap[value], left)
        
        # to get the position of 'right' into the list cmap[value]
        # if 'right' exists on the list, then the right index of the first occurence will be returned
        idx_right = bisect.bisect_right(self.cmap[value], right)
        
        return idx_right - idx_left
           


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)