class Solution:
    # O(n) Time | O(1) Space, where n is length of nums
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        currentSum = 0
        minLength = float("inf")

        while right < len(nums):
            if currentSum >= target:
                minLength = min(minLength, right - left)
                currentSum -= nums[left]
                left += 1
                continue
            currentSum += nums[right]
            right += 1

        while currentSum >= target and left < right:
            minLength = min(minLength, right - left)
            currentSum -= nums[left]
            left += 1
        
        return minLength if minLength != float("inf") else 0
      
