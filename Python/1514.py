from collections import defaultdict
import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dist = edges[i]
            adj[src].append([dist, succProb[i]])
            adj[dist].append([src, succProb[i]])
            
        queue = [(-1,start_node)]
        visited = set()
        while queue:
            prob, curr = heapq.heappop(queue)
            visited.add(curr)
            
            if curr == end_node:
                return prob * -1
            
            for v, edge_prob in adj[curr]:
                if v not in visited:
                    heapq.heappush(queue, (prob * edge_prob, v))
            
        return 0
        
            
            
        