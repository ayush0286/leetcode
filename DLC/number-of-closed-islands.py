# Leetcode https://leetcode.com/problems/number-of-closed-islands
# Notes: mark the land on the border -1, traverse all 0s inside the borders, increase island count on every such new traverse
# JIRA: https://sde2.atlassian.net/browse/UB-8

class Solution:
    # O(mn) Time | O(1) extra Space, where n and m are dimensions of the matrix
    def closedIsland(self, grid: List[List[int]]) -> int:
        # explore borders
        if len(grid) == 0:
            return 0
        for row in [0, len(grid) - 1]:
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    self.explore(grid, row, col)
        
        for col in [0, len(grid[row]) - 1]:
            for row in range(len(grid)):
                if grid[row][col] == 0:
                    self.explore(grid, row, col)
        islandCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    self.explore(grid, row, col)
                    islandCount += 1
        return islandCount


    def explore(self, grid, row, col):
        grid[row][col] = -1
        if row - 1 >= 0 and grid[row -1][col] == 0:
            self.explore(grid, row -1, col)
        if col - 1 >= 0 and grid[row][col - 1] == 0:
            self.explore(grid, row, col - 1)
        if col + 1 < len(grid[row]) and grid[row][col + 1] == 0:
            self.explore(grid, row, col + 1)
        if row + 1 < len(grid) and grid[row + 1][col] == 0:
            self.explore(grid, row + 1, col)
