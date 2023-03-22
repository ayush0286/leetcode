class Solution:
    # O(n) Time | O(1) Space, where n is length of nums
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # push 2 towards end 
        end = len(nums) - 1
        start = 0
        while start <= end:
            if nums[end] == 2:
                end -= 1
            elif nums[start] == 2:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1

        # push 0 towards beginning
        start = 0
        while end >= start:
            if nums[start] == 0:
                start += 1
            elif nums[end] == 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
            else:
                end -= 1
        return nums
