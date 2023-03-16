class Solution:
    # O(n) Time | O(n) Space, where n is length of nums
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        integerIndexes = defaultdict(list)
        for index in range(len(nums)):
            integerIndexes[nums[index]].append(index)
        
        for index in range(len(nums)):
            other = target - nums[index]
            if other in integerIndexes:
                for otherIdx in integerIndexes[other]:
                    if otherIdx != index:
                        return [index, otherIdx]
