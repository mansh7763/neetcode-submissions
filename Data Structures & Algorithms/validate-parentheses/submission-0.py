class Solution:
    def isValid(self, s: str) -> bool:
        flag=0
        if len(s)%2==0:
            n = len(s) 
        else: 
            n = len(s)+1

        for i in range(n//2):
            if s[i] == '(' and s[len(s)-i-1] == ')' or s[i] == ')' and s[len(s)-i-1] == '(':
                flag = 1
            elif s[i] == '{' and s[len(s)-i-1] == '}' or s[i] == '}' and s[len(s)-i-1] == '{':
                flag = 1
            elif s[i] == '[' and s[len(s)-i-1] == ']' or s[i] == ']' and s[len(s)-i-1] == '[':
                flag = 1
            else:
                return False
        return True



        