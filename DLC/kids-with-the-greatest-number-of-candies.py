# Leetcode https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
# Notes: find most candies, compare each kids candies + extra with most candies
# JIRA: https://sde2.atlassian.net/browse/UB-38

class Solution:
    # O(n) Time | O(1) Space, where n is length of candies
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = 0
        for candyCount in candies:
            if candyCount > maximum:
                maximum = candyCount

        result = []
        for candyCount in candies:
            result.append(candyCount + extraCandies >= maximum) 
        return result
