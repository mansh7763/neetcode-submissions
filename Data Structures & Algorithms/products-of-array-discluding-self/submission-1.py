class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for i in nums:
            if i==0:
                continue
            product *= i

        if 0 in nums:
            result = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    result[i] = product
            return result

        result = []
        for i in nums:
            result.append(product//i)
        return result

        
        