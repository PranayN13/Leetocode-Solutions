class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()

        grid = list(zip(*grid))  # <-- transpose grid; rows become cols and cols become rows

        return sum(max(row) for row in grid)
