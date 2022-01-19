class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def heapsort(nums):
            heap = []
            for item in nums:
                heapq.heappush(heap, item)
            return [heapq.heappop(heap) for _ in range(len(heap))]
        
        # call the method heapsort()
        nums_sorted = heapsort(nums)
        count_map = {}
        count = 0
        i = 0 
        for item in nums_sorted:
            if item not in count_map:
                count_map[item] = max(count, i)
                count += 1
            i += 1
        
        return [count_map[num] for num in nums]
        
        
        