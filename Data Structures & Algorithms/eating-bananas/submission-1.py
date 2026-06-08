import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Your correct boundary logic!
        low = 1
        high = max(piles)
        
        # Standard binary search loop
        while low < high:
            mid = (low + high) // 2
            
            # Calculate total time (x) using your logic
            x = 0
            for i in piles:
                x += (i + mid - 1) // mid  # Fast integer ceiling division
            
            # Your adjusted condition logic:
            if x > h:
                # Too slow! We must look for a faster speed to the right.
                low = mid + 1
            else:
                # Safe speed! But can we do even better (smaller)? 
                # Look to the left, keeping 'mid' as a possibility.
                high = mid
                
        # When low == high, we have converged on the minimum valid speed.
        return low