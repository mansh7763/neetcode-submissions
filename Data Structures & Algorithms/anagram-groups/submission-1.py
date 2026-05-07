from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first brute force approach. Time complexity: 0(n^2.klogk)
        # visited = [False] * len(strs)
        # final_result = []

        # for i in range(len(strs)):
        #     if visited[i]:
        #         continue

        #     mid = sorted(strs[i])
        #     result = [strs[i]]
        #     visited[i] = True

        #     for j in range(i + 1, len(strs)):
        #         if not visited[j] and mid == sorted(strs[j]):
        #             result.append(strs[j])
        #             visited[j] = True

        #     final_result.append(result)

        # return final_result

        # Hashmap
        anagram_map = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            anagram_map[key].append(word)
        return list(anagram_map.values())
