import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        while low < high:
            mid = (low + high) // 2
            
            x = 0
            for i in piles:
                x += (i + mid - 1) // mid  # Fast integer ceiling division
            
            if x > h:
                low = mid + 1
            else:
                high = mid
                
        return low