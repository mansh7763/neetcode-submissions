class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for i in range(len(nums)):
            if (nums[i]) in remain:
                result  = [i, remain[nums[i]]]
                return sorted(result)
            else:
                remain[target-nums[i]] = i

        