class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            current = s[right]
            if current in lookup and lookup[current] >= left:
                left = lookup[current]+1
            max_length = max(max_length, right-left+1)

            lookup[current] = right
        return max_length