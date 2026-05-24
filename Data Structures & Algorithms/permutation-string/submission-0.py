class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force
        s1 = sorted(s1)
        left = 0
        right = len(s1)

        while right < len(s2):
            subStr = s2[left: right]
            subStr=sorted(subStr)
            if s1 == subStr:
                return True
            else:
                left+=1
                right+=1
        return False



