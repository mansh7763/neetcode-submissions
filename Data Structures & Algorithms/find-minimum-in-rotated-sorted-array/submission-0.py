class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        for i in range(len(nums)-2):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
        