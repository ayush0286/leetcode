# Leetcode https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# Notes: since values are unique, only one maximum and minimum needs to be evaluated
# JIRA: https://sde2.atlassian.net/browse/UB-66

class Solution:
    # O(n) Time | O(1) Space, where n is length of salary
    def average(self, salary: List[int]) -> float:
        maximum = 0
        minimum = float("inf")
        total = 0
        for wage in salary:
            if wage > maximum:
                maximum = wage
            if wage < minimum:
                minimum = wage
            total += wage

        total -= (minimum + maximum)
        return total / (len(salary) - 2)  
