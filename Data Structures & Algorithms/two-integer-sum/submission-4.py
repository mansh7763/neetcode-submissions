class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Kadane Algorithm
        remain = {}
        for i in range(len(nums)):
            if (nums[i]) in remain:
                return [remain[nums[i]], i]
            else:
                remain[target-nums[i]] = i

        # # Brute Force: Time=0(n^2), space=0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == target - nums[j]:
        #             return [i, j]

        