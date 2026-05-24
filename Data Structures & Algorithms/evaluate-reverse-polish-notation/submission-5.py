class Solution:

    def calculation(self, left, operator, right):
        if operator == '+':
            return int(left + right)
        elif operator == '-':
            return int(left - right)
        elif operator == '*':
            return int(left * right)
        elif operator == "/":
            return int(left / right)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 1

        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                right = stack.pop()
                left = stack.pop()

                result = self.calculation(left, i, right)
                stack.append(result)

        return stack[-1]