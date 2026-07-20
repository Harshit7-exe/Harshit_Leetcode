class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        total = rows * cols

        k %= total

        ans = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                old_index = r * cols + c
                new_index = (old_index + k) % total

                new_r = new_index // cols
                new_c = new_index % cols

                ans[new_r][new_c] = grid[r][c]

        return ans