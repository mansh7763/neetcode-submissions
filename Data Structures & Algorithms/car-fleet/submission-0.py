class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i, j in zip(position, speed):
            remaining_dist = target - i
            time.append(remaining_dist//j)
        return len(list(set(time)))

        