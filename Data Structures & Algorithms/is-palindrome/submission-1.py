class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = "".join(ch.lower() for ch in s if ch.isalnum())
        for i in range(len(alnum)//2):
            if alnum[i] != alnum[len(alnum)-1-i]:
                return False
        return True
        