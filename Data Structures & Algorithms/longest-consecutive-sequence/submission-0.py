class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums, reverse=True)
        count = 1
        max_count = 1
        for i in range(len(nums)-1):
            if sorted_nums[i+1] == sorted_nums[i]:
                continue
            elif sorted_nums[i+1] == sorted_nums[i]-1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
        return max_count

        