class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights)-1
        max_water = 0
        while first <= last:
            if heights[first] > heights[last]:
                water = heights[last]*(last-first)
                max_water = max(water, max_water)
                last -= 1
            else:
                water = heights[first]*(last-first)
                max_water = max(water, max_water)
                first += 1
        return max_water
            
