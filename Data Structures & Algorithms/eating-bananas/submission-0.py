class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        k = 1

        while True:
            result = 0
            for i in piles:
                if i % k == 0:
                    result = result + (i // k) 
                else:
                    result = result + (i // k + 1)
            if result <= h: 
                return k
            k = k + 1