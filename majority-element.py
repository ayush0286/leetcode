class Solution:
    # O(n) Time | O(1) Space, where n is length of nums
    def majorityElement(self, nums: List[int]) -> int:

        count = 1
        majority = nums[0]
        
        for num in nums[1:]:
            if num == majority:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority = num
                count = 1
        return majority
