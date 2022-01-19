class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapsort(nums):
            heap = []
            for item in nums:
                heapq.heappush(heap, item)
            return [heapq.heappop(heap) for _ in range(len(nums))]
        
        # call the method heapsort() and return the kth elemnet from the last
        return heapsort(nums)[-k]