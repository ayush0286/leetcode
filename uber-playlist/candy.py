# Leetcode https://leetcode.com/problems/candy/
# Notes: find mins, find length of mins, sort by lengths, start from greatest and carefully fill candies 
# JIRA: https://sde2.atlassian.net/browse/UB-69

class Solution:
    # O(n) Time | O(n) Space, where n is length of ratings
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)
        if len(ratings) == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3
        # find mins
        minIndexes = self.findMinIndexes(ratings)
        if len(minIndexes) == 0:
            return len(ratings)
        # find min lengths left and right
        lengthAndMins = []
        for minIndex in minIndexes:
            leftLength = self.minLengthsLeft(minIndex, ratings)
            rightLength = self.minLengthsRight(minIndex, ratings)
            lengthAndMins.append([max(leftLength, rightLength), minIndex])
        lengthAndMins.sort()
        # fill the candies, lengthiest min at a time
        candies = self.fillCandies(lengthAndMins, ratings)
        return sum(candies)

    def fillCandies(self, lengthAndMinIndexes, ratings):
        candies = [1 for index in range(len(ratings))]
        for length, index in reversed(lengthAndMinIndexes):
            # left fill
            currIdx = index - 1
            if currIdx >= 0 and candies[currIdx] <= candies[currIdx + 1]:
                while currIdx >= 0 and ratings[currIdx] > ratings[currIdx + 1]:
                    if candies[currIdx] <= candies[currIdx + 1]:
                        candies[currIdx] = candies[currIdx + 1] + 1
                    currIdx -= 1

            #right fill
            currIdx = index + 1
            if currIdx < len(ratings) and candies[currIdx] <= candies[currIdx - 1]:
                while currIdx < len(ratings) and ratings[currIdx] > ratings[currIdx - 1]:
                    if candies[currIdx] <= candies[currIdx - 1]:
                        candies[currIdx] = candies[currIdx - 1] + 1
                    currIdx += 1
        return candies

    def minLengthsLeft(self, index, ratings):
        length = 0
        while index > 0 and ratings[index] < ratings[index - 1]:
            length += 1
            index -= 1
        return length
    
    def minLengthsRight(self, index, ratings):
        length = 0
        while index < len(ratings) - 1 and ratings[index] < ratings[index + 1]:
            length += 1
            index += 1
        return length
    
    
    def findMinIndexes(self, ratings):
        minIndexes = []
        if ratings[0] < ratings[1]:
            minIndexes.append(0)
        for index in range(1, len(ratings) - 1):
            if ratings[index] < ratings[index + 1] and ratings[index] < ratings[index - 1]:
                minIndexes.append(index)
            elif ratings[index] < ratings[index + 1] and ratings[index] == ratings[index - 1]:
                minIndexes.append(index)
            elif ratings[index] == ratings[index + 1] and ratings[index] < ratings[index - 1]:
                minIndexes.append(index)
        if len(ratings) > 2:
            if ratings[-1] < ratings[-2]:
                minIndexes.append(len(ratings) - 1)
        return minIndexes
    
    
