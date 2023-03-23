class Solution:
    # O(nlogn) Time | O(n) Space, where n is length of nums
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # traverse right to left
        # find the first digit that breaks the decreasing order
        # find the next big digit to it
        # swap with the next big digit
        # ascending order sort the remaining
        
        index = len(nums) - 1
        while index > 0:
            if nums[index] > nums[index - 1]:
                break
            index -= 1
        if index == 0:
            nums.sort()
            return nums
        index -= 1
        partialArray = nums[index:]
        partialArray.sort()

        nextDigit = None
        for idx in range(len(partialArray)):
            if partialArray[idx] > nums[index]:
                nextDigit = partialArray[idx]
                break
        nums[index] = nextDigit
        index += 1
        foundRepeat = False
        for idx in range(len(partialArray)):
            if partialArray[idx] == nextDigit and not foundRepeat:
                foundRepeat = True
                continue
            nums[index] = partialArray[idx]
            index += 1
        return nums
        
