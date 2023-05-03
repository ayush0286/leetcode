# Leetcode https://leetcode.com/problems/candy/
# Notes: find mins, find length of mins, sort by lengths, start from greatest and carefully fill candies 
# JIRA: https://sde2.atlassian.net/browse/UB-69

class Solution:
    # O(n) Time | O(n) Space, where n is length of ratings
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for rating in ratings]
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index - 1]:
                candies[index] = candies[index - 1] + 1
        
        for index in reversed(range(len(ratings) - 1)):
            if ratings[index] > ratings[index + 1]:
                if candies[index] < candies[index + 1] + 1:
                    candies[index] = candies[index + 1] + 1
        return sum(candies)
