class Solution:
    def productExceptSelf(self, nums):
        product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        result = [0] * len(nums)

        if zero_count > 1:
            return result   # all zeros

        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result[i] = product
            return result

        # no zeros
        for i in range(len(nums)):
            result[i] = product // nums[i]

        return result