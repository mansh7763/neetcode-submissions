class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []   # (temperature, index)
        result = []

        n = len(temperatures)

        for i in range(n - 1, -1, -1):

            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if not stack:
                result.append(0)
            else:
                result.append(stack[-1][1] - i)

            stack.append((temperatures[i], i))

        return result[::-1]