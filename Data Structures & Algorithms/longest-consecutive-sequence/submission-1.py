class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_count = 0

        for num in nums_set:

            # start of sequence
            if num - 1 not in nums_set:

                current = num
                count = 1

                while current + 1 in nums_set:
                    current += 1
                    count += 1

                max_count = max(max_count, count)

        return max_count