class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        r, c = 0, (col - 1)
        while (r <= c):
            if matrix[r][c] == target: return True
            elif matrix[r][c] > target: c = c-1
            else: r = r + 1
        return False