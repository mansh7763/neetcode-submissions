class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for i in range(len(nums)):
            if (nums[i]) in remain:
                return i, remain[nums[i]]
            else:
                remain[target-nums[i]] = i

        