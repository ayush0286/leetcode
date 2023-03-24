class Solution:
    O(m + n) Time | O(m + n) Space
    def uniquePaths(self, m: int, n: int) -> int:
        downCount = m - 1
        rightCount = n - 1

        numerator = self.factorial(rightCount + downCount) 
        denominator = self.factorial(rightCount) * self.factorial(downCount)
        return numerator // denominator

    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        return n * self.factorial(n - 1)
