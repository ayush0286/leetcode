# Leetcode https://leetcode.com/problems/successful-pairs-of-spells-and-potions
# Notes: sorting the potions, optimizes the problem
# JIRA: https://sde2.atlassian.net/browse/UB-3

class Solution:
    # O(nlogm + mlogm) Time | O(n) Space, where n is length of spells and m is length 
    # of potions
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        for spell in spells:
            startIndex = self.findFirstSuccesfulPotionIndex(spell, potions, success)
            if startIndex is None:
                pairs.append(0)
            else:
                pairCount = len(potions) - startIndex
                pairs.append(pairCount)
        return pairs

    def findFirstSuccesfulPotionIndex(self, spell, potions, target):
        left = 0
        right = len(potions) - 1
        index = None
        while left <= right:
            mid = (left + right) // 2
            if spell * potions[mid] >= target:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
        return index
