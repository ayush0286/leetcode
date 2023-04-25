# Leetcode https://leetcode.com/problems/last-stone-weight/
# Notes: insert numbers into max heap, iterate over maxHeap till goal is reached
# JIRA: https://sde2.atlassian.net/browse/UB-59

class Solution:
    # O(nlogn) Time | O(n) Space, where n is length of stones
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for weight in stones:
            heapq.heappush(heap, -1 * weight)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if second - first != 0:
                heapq.heappush(heap, ( first - second))
            
        return -1 * heapq.heappop(heap) if len(heap) == 1 else 0
