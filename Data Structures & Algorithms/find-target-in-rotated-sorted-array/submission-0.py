from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target: 
                return mid
            
            # Identify the sorted half
            # Case 1: Right half is sorted
            if nums[mid] <= nums[high]:
                # Added '=' to nums[high] >= target
                if nums[mid] < target and target <= nums[high]: 
                    low = mid + 1
                else: 
                    high = mid - 1
            
            # Case 2: Left half is sorted
            else:
                # Added '=' to nums[low] <= target
                if nums[low] <= target and target < nums[mid]: 
                    high = mid - 1
                else: 
                    low = mid + 1
                    
        return -1  # Return -1 if target is not found