# Leetcode https://leetcode.com/problems/rearranging-fruits
# Notes: swapping can be minimized by double swapping smallest value 
# JIRA: https://sde2.atlassian.net/browse/UB-47

class Solution:
    # O(nlogn) Time | O(n) Space, where n is length of basket1
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        basket1.sort()
        basket2.sort()
        values = defaultdict(int)
        for value in basket1:
            values[value] += 1
        for value in basket2:
            values[value] -= 1
        
        discard1, discard2 = self.populateDiscardPiles(values)
        if discard1 is None or len(discard1) != len(discard2):
            return -1

        smallest = min(basket1[0], basket2[0])
        return self.calculateMinCost(discard1, discard2, smallest)


    def calculateMinCost(self, discard1, discard2, smallest):
        cost = 0
        left = 0
        right = len(discard2) - 1
        while left < right:
            cost1 = min(min(discard1[left], discard2[right]), 2 * smallest)
            cost2 = min(min(discard2[left], discard1[right]), 2 * smallest)
            cost += cost1 + cost2
            left += 1
            right -= 1
            
        if left == right:
            cost += min(min(discard1[left], discard2[right]), 2 * smallest)
        return cost


    def populateDiscardPiles(self, values):
        discard1 = []
        discard2 = []
        for key in values:
            value = values[key]
            if abs(value) % 2 != 0:
                return [None, None]
            if value < 0:
                for index in range(abs(value) // 2):
                    discard2.append(key)
            elif value > 0:
                for index in range(value // 2):
                    discard1.append(key)
        discard1.sort()
        discard2.sort()
        return [discard1, discard2]
        
