class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Time complexity O(n^2) and space O(n)

        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        
        # for constant O(1) lookup time for duplicate: hashset

        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

        