class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # identify the sorted half
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target: 
                return mid

            # case 1: Right half is sorted
            if nums[mid] <= nums[high]:
                if nums[mid] < target and target <= nums[high]: 
                    low = mid + 1
                else: 
                    high = mid - 1
            
            # Case 2: Left half is sorted
            else:
                if nums[low] <= target and target < nums[mid]: 
                    high = mid - 1
                else: 
                    low = mid + 1
                    
        return -1