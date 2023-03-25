class Solution:
    # O(n) Time | O(n) Space, where n is length of nums
    def longestConsecutive(self, nums: List[int]) -> int:
        numIndexes = {}
        prevNumIndexes = [-1 for index in range(len(nums))]
        soFarLengths = {}
        longestLength = 0

        for index in range(len(nums)):
            numIndexes[nums[index]] = index

        for index in range(len(nums)):
            num = nums[index]
            # add jump index
            if num - 1 in numIndexes:
                prevNumIndexes[index] = numIndexes[num - 1]

        for index in range(len(prevNumIndexes)):
            if prevNumIndexes[index] == -1:
                continue
            currLength = self.getSoFarLength(index, prevNumIndexes, soFarLengths)
            soFarLengths[index] = currLength
            longestLength = max(longestLength, soFarLengths[index])
        if len(nums) >= 1 and longestLength == 0:
            return 1
        return longestLength

    def getSoFarLength(self, index, nextIndexes, memo):
        if index == -1:
            return 0
        if index in memo:
            return memo[index]
        
        nextIndex = nextIndexes[index]
        nextLength = self.getSoFarLength(nextIndex, nextIndexes, memo)
        memo[index] = nextLength + 1
        return memo[index]
