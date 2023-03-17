class Solution:
    # O(logn) Time | O(logn) space, where n is length of nums
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        endPoints = [-1, -1]
        endPoints = self.binarySearch(0, len(nums) - 1, nums, target, endPoints, None)
        return endPoints
        
    def binarySearch(self, left, right, nums, target, endPoints, direction):
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                if direction is None:
                    endPoints = [middle, middle]
                    if middle - 1 >= 0 and nums[middle - 1] == target:
                        endPoints = self.binarySearch(left, middle - 1, nums, target, endPoints, 'left')
                    if middle + 1 < len(nums) and nums[middle + 1] == target:
                        endPoints = self.binarySearch(middle + 1, right, nums, target, endPoints, 'right')
                    break
                elif direction == 'left':
                    endPoints[0] = middle
                    if middle - 1 >= 0 and nums[middle - 1] == target:
                        endPoints = self.binarySearch(left, middle - 1, nums, target, endPoints, 'left')
                    break
                else: # direction == 'right'
                    endPoints[1] = middle
                    if middle + 1 < len(nums) and nums[middle + 1] == target:
                        endPoints = self.binarySearch(middle + 1, right, nums, target, endPoints, 'right')
                    break
            elif target > nums[middle]:
                left = middle + 1
            else: # target < nums[middle]
                right = middle - 1
        return endPoints
    
