# Leetcode https://leetcode.com/problems/number-of-enclaves
# Notes: mark all the boundary land as  -1 with traversal, find all the remaining 1s
# JIRA: https://sde2.atlassian.net/browse/UB-12

class Solution:
    # O(mn) Time | O(1) Space, where m and n are dimensions of grid
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        for row in [0, len(grid) - 1]:
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    self.explore(grid, row, col)
        
        for col in [0, len(grid[row]) - 1]:
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    self.explore(grid, row, col)
        
        landCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    landCount += 1
        return landCount

    def explore(self, grid, row, col):
        grid[row][col] = 2
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            self.explore(grid, row - 1, col)
        if row + 1 < len(grid) and grid[row + 1][col] == 1:
            self.explore(grid, row + 1, col)
        if col + 1 < len(grid[row]) and grid[row][col + 1] == 1:
            self.explore(grid, row, col + 1)
        if col - 1 >= 0 and grid[row][col - 1] == 1:
            self.explore(grid, row, col - 1)
     
