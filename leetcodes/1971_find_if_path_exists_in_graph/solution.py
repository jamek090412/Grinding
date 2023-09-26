from collections import defaultdict, deque
from typing import List
"""
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""
class Solution:
  def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
    return self.using_bfs(n, edges, start, end)

  def build_graph(self, edges: List[List[int]]):
    g = defaultdict(list)
    for e1, e2 in edges:
      g[e1].append(e2)
      g[e2].append(e1)
    return g
  
  def using_bfs(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
    graph, visited, queue = self.build_graph(edges), set(), deque([start])

    while queue:
      cur = queue.popleft()
      if cur == end:
        return True

      for adj in graph[cur]:
        if adj not in visited:
          visited.add(cur)
          queue.append(adj)

    return False

  def using_dfs(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
    graph, visited = self.build_graph(edges), set()
    pass

  def using_uf(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
    
    pass
    
