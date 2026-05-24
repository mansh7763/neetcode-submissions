class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n == m:
            for i in range(n):
                flag = 0
                for j in range(n):
                    if s[i] == t[j]:
                        flag = 1
                if flag != 1:
                    return False
            return True
        else:
            return False