class Solution:
    # O(n) Time | O(1) Space, where n is length of nums
    def findDuplicate(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            num = abs(nums[index])
            if nums[num - 1] < 0:
                return num
            else:
                nums[num - 1] *= -1
