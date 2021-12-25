class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left_pivot = 0
        right_pivot = len(height)-1
        
        while left_pivot != right_pivot:
            current_area = abs(right_pivot-left_pivot) * min(height[left_pivot], height[right_pivot])
            
            # update the area
            if  current_area > area:
                area = current_area
            
            #update the pivots
            if height[left_pivot] < height[right_pivot]:
                left_pivot += 1
            else:
                right_pivot -= 1
            
        return area
        