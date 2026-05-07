class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Kadane Algorithm
        remain = {}
        for i in range(len(nums)):
            if (nums[i]) in remain:
                result  = [i, remain[nums[i]]]
                return sorted(result)
            else:
                remain[target-nums[i]] = i
        # Brute Force
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == target - nums[j]:
                    return [i, j]

        