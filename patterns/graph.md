# Graph
## Prerequisites
### Adjacency List
```python
def build_graph(edges: List[List[int]]):
  g = defaultdict(list)
  for e1, e2 in edges:
    g[e1].append(e2)
    g[e2].append(e1)
  return g
```

## DFS
- Traverse all vertices in a "graph"
- Traverse all paths between any two vertices in a "graph"

## BFS
- Traverse all vertices in a "graph"
- Find the shortest path between two vertices in a "graph"
  - where all edges have equal and positive weights.
  
## Topological Sort (Kahn's algorithm)
- Find a linear ordering of elements that have dependencies on each other.
  - For example, if event 'B' is dependent on event 'A', 'A' comes before 'B' in topological ordering.

Topological Sort of a **directed** graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex `U` to vertex `V`, `U` comes before `V` in the ordering.
- "Topological sorting" only works with graphs that are **directed** and **acyclic**.
- There is at least one vertex in the "graph" with an "in-degree" of 0.
  - If all vertices in the “graph” have non-zero "in-degree", then all vertices need at least one vertex as a predecessor. In this case, no vertex can serve as the starting vertex.

### Algorithm

- In-degree: count of incoming edges of each vertex.
  - Any vertex with '0' in-degree is a source.


#### a. Initialization
1. Store the graph in **Adjacency Lists**, which means each parent vertex will have a list containing all of its children. 
	- We will do this using a **HashMap** 
		- where the 'key' will be the parent vertex number and 
		- the 'value' will be a **List** containing children vertices.
2. To find the sources, we will keep a **HashMap** to count the in-degrees 

#### b. Build the graph and find in-degrees of all vertices
1. Build the graph from the input and populate the in-degrees **HashMap**.

#### c. Find all sources - BFS
1. All vertices with '0' in-degrees will be our sources and we will store them in a **Queue**.

#### d. Sort
1.  For each source, do the following things:
    -   Add it to the sorted list.
    -   Get all of its children from the graph.
    -   Decrement the in-degree of each child by 1.
    -   If a child’s in-degree becomes ‘0’, add it to the sources **Queue**.
2.  Repeat step 1, until the source **Queue** is empty.

BFS
```python
from collections import deque

def topological_sort(vertices, edges):
	sortedOrder = []
	if vertices <= 0:
		return sortedOrder

	# a. Initialize the graph
	inDegree = {i: 0 for i in range(vertices)} # count of incoming edges
	graph = {i: [] for i in range(vertices)} # adjacency list graph

	# b. Build the graph
	for edge in edges:
		parent, child = edge[0], edge[1]
		graph[parent].append(child) # put the child into it's parent's list
		inDegree[child] += 1 # increment child's inDegree

	# c. Find all sources i.e., all vertices with 0 in-degrees
	sources = deque()
	for key in inDegree:
		if inDegree[key] == 0:
			sources.append(key)

	# d. For each source, add it to the sortedOrder and 
	#      subtract one from all of its children's in-degrees 
	#	 if a child's in-degree becomes zero, add it to the sources queue
	while sources:
		vertex = sources.popleft()
		sortedOrder.append(vertex)
		for child in graph[vertex]: 
			# get the node's children to decrement their in-degrees
			inDegree[child] -= 1
			if inDegree[child] == 0:
				sources.append(child)

	# topological sort is not possible as the graph has a cycle
	if len(sortedOrder) != vertices:
		return []

 return sortedOrder
```

## Single Source Shortest Path problem 
refers to "Given the starting vertex, find the 'shortest path' to any of the vertices in a **weighted** graph. 
Once we solve this, we can easily acquire the shortest paths between the starting vertex and a given target vertex.

- BFS algorithm can only solve the "shortest path" problem in "unweighted graph"
- But in real life, we often need to find the "shortest path" in a "weighted graph".

### Edge Relaxation 
Edge Relaxation operation is a key element in solving the "single-source shortest path" problem.

Two Algorithms
- Dijkstra
  - can only be used to solve the "single-source shortest path" problem in a graph with **non-negative** weights.
- Bellman-Ford
  - can solve the "single-source shortest path" in a weighted directed graph with **any weights**, including, of course, **negative** weights.

### Dijakstra

```python

```

### Bellman-Ford


## Union Find
- Check connectivity between two vertices 

```python

```

## Minimum Spanning Tree

[1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points)



```python

```

# Related

## Tree

## Grid / Matrix

## Backtracking

## Stack and Queue

# Exercises

#### [1971. Find if Path exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) - Easy
##### DFS
```python
def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
  graph, visited = build_graph(edges), set()

  def dfs(v):
    if v in visited:
      return False
    else:
      visited.add(v)

		if v == end:
      return True

		for vertex in graph[v]:
			if dfs(vertex):
				return True

		return False

	return dfs(start)
```

##### BFS
```python
def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
	visited, graph, queue = set(), build_graph(edges), deque([start])
	 
	while queue:
		cur = queue.popleft()
		if cur == end:
			return True

		for adj in graph[cur]:
			if adj not in visited: 
				visited.add(cur)
				queue.append(adj)

	return False
```

##### Union Find
```python
def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
	uf = UnionFind(n)

	for edge in edges:
		uf.union(edge[0], edge[1])
	return uf.find(source) == uf.find(destination)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
```

