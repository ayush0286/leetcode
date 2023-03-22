class Solution:
    # O(n) Time | O(1) Space, where n is length of nums
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        runningSum = 0
        total = 0

        # finding maximum subarray sum
        for num in nums:
            total += num
            if num >= 0:
                runningSum += num
                maxSum = max(runningSum, maxSum)
            else: # num < 0
                newRunningSum = runningSum + num
                if newRunningSum >= 0:
                    runningSum += num
                    maxSum = max(runningSum, maxSum)
                else:
                    runningSum = 0
        maxSum = max(maxSum, runningSum)

        # checking if all numbers are negative in the array
        maxNumber = float('-inf')
        for num in nums:
            maxNumber = max(maxNumber, num)

        return maxNumber if maxNumber < 0 else maxSum
