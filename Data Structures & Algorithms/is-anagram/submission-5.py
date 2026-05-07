class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time complexity: nlog(n) + mlog(m)
        # s = sorted(s) # nlog(n)
        # t = sorted(t) # mlog(m)

        # if s==t:
        #     return True
        # else:
        #     return False

        #hashtable

        if len(s) == len(t):
            freq1 = {}

            for i in s:
                if i in freq1:
                    freq1[i] += 1
                else:
                    freq1[i] = 1

            freq2 = {}

            for j in t:
                if j in freq2:
                    freq2[j] += 1
                else:
                    freq2[j] = 1
            
            for i in freq1:
                if i in freq2:
                    if freq1[i] != freq2[i]:
                        return False
                else:
                    return False           
            return True
        else:
            return False