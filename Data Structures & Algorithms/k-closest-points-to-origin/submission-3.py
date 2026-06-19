class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for xi, yi in points:
            cur_dist = math.sqrt((xi)**2 + (yi)**2)
            if len(max_heap) < k:
                heapq.heappush_max(max_heap, (cur_dist, [xi, yi]))
            else:
                if max_heap[0][0] > cur_dist:
                    heapq.heappop_max(max_heap)
                    heapq.heappush_max(max_heap, (cur_dist, [xi, yi]))
        return [item[1] for item in max_heap]


