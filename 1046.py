import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        steiner = [-stone for stone in stones]
        
        heapq.heapify(steiner)

        while len(steiner) > 1:
            y = -heapq.heappop(steiner)
            x = -heapq.heappop(steiner)

            if y != x:
                heapq.heappush(steiner, -(y - x))

        return -steiner[0] if steiner else 0
    