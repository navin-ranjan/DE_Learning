# Data Structures & Algorithms Theory

This file provides comprehensive theory explanations for Data Structures & Algorithms, mapped to the syllabus in `README.md`. Each section includes conceptual explanations, practical examples, and relevance to data engineering.

## Table of Contents
1. [Core Theory Concepts](#1-core-theory-concepts)
2. [Linear Data Structures](#2-linear-data-structures)
3. [Non-Linear Data Structures](#3-non-linear-data-structures)
4. [Searching Algorithms](#4-searching-algorithms)
5. [Sorting Algorithms](#5-sorting-algorithms)
6. [Graph Algorithms](#6-graph-algorithms)
7. [Dynamic Programming](#7-dynamic-programming)
8. [Recursion \& Backtracking](#8-recursion--backtracking)
9. [Greedy Algorithms](#9-greedy-algorithms)
10. [Complexity Analysis](#10-complexity-analysis)
11. [Problem Solving Patterns](#11-problem-solving-patterns)
12. [Python Implementation Focus](#12-python-implementation-focus)

---

## 1. Core Theory Concepts

### 📖 What are Core Theory Concepts?

**Core Theory Concepts** form the mathematical and conceptual foundation needed to understand how data structures and algorithms work under the hood. These concepts help you analyze trade-offs, choose the right approach, and understand why certain implementations perform better than others.

**Key Concepts:**

- **Abstract Data Type (ADT)**: A mathematical model that defines a data type by its behavior (operations) rather than its implementation. Examples include Stack, Queue, List, and Map. The ADT specifies WHAT operations are available, not HOW they are implemented.

- **Concrete Implementation**: The actual code that implements an ADT. For example, a Stack can be implemented using an array (list in Python) or a linked list.

- **Time-Space Tradeoff**: The principle that optimizing for time complexity often requires more space (memory) and vice versa. For example, caching results (memoization) speeds up computation but uses more memory.

- **Amortized Analysis**: A method for analyzing the average time per operation over a sequence of operations, rather than worst-case for a single operation. Example: dynamic array resizing has O(1) amortized insert cost.

- **Recurrence Relations**: Equations that define a sequence recursively. Used to analyze recursive algorithm complexity. Example: T(n) = 2T(n/2) + O(n) for merge sort.

- **Complexity Classes**: Categories of algorithms based on their time/space complexity:
  - O(1) - Constant
  - O(log n) - Logarithmic
  - O(n) - Linear
  - O(n log n) - Linearithmic
  - O(n²) - Quadratic
  - O(2^n) - Exponential

- **Data Locality**: The principle that accessing memory locations that are close together is faster than accessing distant ones. Cache-aware algorithms exploit this for better real-world performance.

- **Stability in Sorting**: A sorting algorithm is stable if it preserves the relative order of equal elements. Important when sorting by multiple keys.

- **In-Place Algorithms**: Algorithms that use O(1) extra space (or O(log n) for recursion stack).

- **External-Memory Thinking**: Designing algorithms that work efficiently with data that doesn't fit in memory (streaming, chunked processing, disk-based operations).

- **Probabilistic Data Structures**: Data structures that use randomness to achieve space efficiency with a small probability of error:
  - **Bloom Filter**: Space-efficient set membership tester (may have false positives, never false negatives)
  - **HyperLogLog**: Estimates cardinalities of large sets with minimal memory

**Why is this important for Data Engineering?**

- Understanding ADTs helps you choose the right data structure for your use case
- Time-space tradeoffs inform resource planning for ETL pipelines
- Amortized analysis helps predict performance for batch processing
- Data locality matters when processing large datasets that don't fit in memory
- External-memory thinking is essential for working with big data frameworks
- Probabilistic structures are used in streaming analytics and deduplication

---

## 2. Linear Data Structures

### 📖 What are Linear Data Structures?

**Linear Data Structures** are data structures that store elements in a sequential manner, where each element is connected to its previous and next element. Elements are arranged in a linear order and can be traversed in a single pass.

**Key Concepts:**

| Data Structure | Access | Search | Insert | Delete | Use Case |
|----------------|--------|--------|--------|--------|----------|
| **Array** | O(1) | O(n) | O(n) | O(n) | Fast access, fixed size |
| **Linked List** | O(n) | O(n) | O(1)* | O(1)* | Frequent insert/delete |
| **Stack** | O(n) | O(n) | O(1) | O(1) | LIFO operations, parsing |
| **Queue** | O(n) | O(n) | O(1) | O(1) | FIFO operations, BFS |
| **Hash Table** | N/A | O(1)** | O(1)** | O(1)** | Fast lookup |

*At head/tail with pointer
**Average case, O(n) worst case

**Why is this important for Data Engineering?**

- Arrays are the foundation for dataframe columns and numpy arrays
- Linked lists are used in file systems and memory management
- Stacks are essential for expression evaluation and transaction rollback
- Queues are core to message passing and task scheduling
- Hash tables are used for joins, aggregations, and index lookups

### Arrays

**Arrays** are contiguous memory locations that store elements of the same type. They provide O(1) random access by index.

```python
# Creating arrays
arr = [1, 2, 3, 4, 5]           # Simple array
arr2d = [[1, 2, 3], [4, 5, 6]]  # 2D array

# Accessing elements - O(1)
print(arr[0])    # First element
print(arr[-1])   # Last element

# Slicing - O(k) where k is slice size
print(arr[1:4])  # Elements at index 1, 2, 3

# Dynamic array (Python list)
dynamic = []     # Starts empty, grows as needed
for i in range(10):
    dynamic.append(i)  # Amortized O(1) per append
```

### Linked Lists

**Linked Lists** consist of nodes where each node contains data and a reference to the next node. They allow O(1) insertion/deletion at known positions.

```python
# Node definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Singly linked list operations
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Traverse - O(n)
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next

# Insert at head - O(1)
def insert_at_head(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# Delete node - O(1) at head
def delete_at_head(head):
    return head.next if head else None
```

### Stacks

**Stacks** follow the Last-In-First-Out (LIFO) principle. Think of a stack of plates.

```python
# Stack using list
stack = []

# Push - O(1)
stack.append(1)
stack.append(2)
stack.append(3)

# Pop - O(1)
top = stack.pop()  # Returns 3

# Peek - O(1)
top = stack[-1]    # Returns 2 without removing

# Check empty
is_empty = len(stack) == 0
```

### Queues

**Queues** follow the First-In-First-Out (FIFO) principle. Think of a line at a store.

```python
from collections import deque

# Queue using deque - O(1) for both ends
queue = deque()

# Enqueue - O(1)
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue - O(1)
front = queue.popleft()  # Returns 1

# Peek
front = queue[0]  # Returns 2 without removing

# Circular queue (efficient for fixed size)
from collections import deque
circular = deque(maxlen=5)  # Auto-overwrites oldest
```

### Hash Tables / Hash Maps

**Hash Tables** use a hash function to compute an index into an array of buckets, enabling O(1) average-case lookup, insert, and delete.

```python
# Hash map
hash_map = {}

# Insert - O(1) average
hash_map["key1"] = "value1"
hash_map["key2"] = "value2"

# Lookup - O(1) average
value = hash_map["key1"]

# Check existence - O(1) average
if "key1" in hash_map:
    print("Found")

# Collision handling (Python uses open addressing with probing)
# Load factor = n/k where n is entries, k is buckets
# Python resize when load factor > 2/3

# Common operations
hash_map.get("key", "default")  # Safe get
hash_map.keys()                  # All keys
hash_map.values()                # All values
hash_map.items()                 # Key-value pairs
```

### Sets

**Sets** are unordered collections of unique elements, implemented using hash tables.

```python
# Creating sets
s = {1, 2, 3}
s = set([1, 2, 2, 3])  # {1, 2, 3}

# Set operations - O(1) average
s.add(4)           # Add element
s.remove(3)        # Remove (raises if not found)
s.discard(3)       # Remove (no error if not found)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b           # {1, 2, 3, 4, 5, 6}
intersection = a & b    # {3, 4}
difference = a - b      # {1, 2}
sym_diff = a ^ b       # {1, 2, 5, 6}
```

---

## 3. Non-Linear Data Structures

### 📖 What are Non-Linear Data Structures?

**Non-Linear Data Structures** store elements in a hierarchical or interconnected manner, where each element can have multiple relationships with other elements. They are essential for representing hierarchical data, networks, and performing efficient searches.

**Key Concepts:**

- **Trees**: Hierarchical structures with parent-child relationships
- **Graphs**: Networks with arbitrary connections between nodes
- **Hierarchical Access**: Unlike linear structures, you need special traversals (DFS, BFS)

**Why is this important for Data Engineering?**

- Trees are used in databases (B+ trees for indexing)
- Graphs model social networks, dependencies, and routing
- Heaps are used in priority queues and top-k problems
- Tries enable efficient prefix matching (autocomplete)

### Trees

**Trees** are hierarchical data structures with a root node and child nodes. Each node has exactly one parent (except root).

```python
# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Binary Search Tree (BST) - O(log n) average for search/insert/delete
class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        current = self.root
        while True:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    return
                current = current.right

    def search(self, val):
        current = self.root
        while current:
            if val == current.val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False
```

### Balanced Trees (AVL, Red-Black)

**Balanced Trees** automatically rebalance to maintain O(log n) operations even in worst case.

```python
# AVL Tree - height-balanced BST
# Rotations: LL, RR, LR, RL to maintain balance
# Balance factor = height(left) - height(right) ∈ {-1, 0, 1}

# Red-Black Tree - self-balancing BST
# Properties:
# 1. Every node is red or black
# 2. Root is black
# 3. Every leaf (NIL) is black
# 4. Red node can't have red children
# 5. Every path has same number of black nodes
# Guarantees O(log n) operations
```

### Heaps

**Heaps** are complete binary trees that satisfy the heap property: parent is always greater (max heap) or smaller (min heap) than children.

```python
import heapq

# Min Heap - smallest element at root
min_heap = []

# Push - O(log n)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 7)

# Pop - O(log n)
smallest = heapq.heappop(min_heap)  # Returns 3

# Heapify - O(n)
arr = [5, 3, 7, 1, 9]
heapq.heapify(arr)

# Max Heap (negate values)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
max_val = -heapq.heappop(max_heap)  # Returns 5

# Top K elements - O(n log k)
def top_k(arr, k):
    return heapq.nlargest(k, arr)
```

### Graphs

**Graphs** consist of vertices (nodes) connected by edges. Can be directed/undirected, weighted/unweighted.

```python
from collections import defaultdict, deque

# Graph representation
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)  # Adjacency list

    def add_edge(self, u, v, directed=False):
        self.adj[u].append(v)
        if not directed:
            self.adj[v].append(u)

    # BFS - O(V + E)
    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    # DFS - O(V + E)
    def dfs(self, start):
        visited = set()
        result = []

        def dfs_util(node):
            visited.add(node)
            result.append(node)

            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)
        return result
```

### Tries (Prefix Tree)

**Tries** are tree structures used for efficient prefix matching and autocomplete.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

### B-Trees & B+ Trees

**B-Trees** are self-balancing trees optimized for disk access, used in databases and file systems.

```python
# B+ Tree characteristics:
# - All data stored at leaf nodes
# - Leaf nodes linked for range queries
# - Optimized for sequential access
# - Used in databases (MySQL InnoDB, PostgreSQL)
# - Order (m): Each node has at most m children

# Why B+ Trees for databases:
# 1. Fanout reduces tree height
# 2. All data in leaves = efficient range queries
# 3. Linked leaves = sequential disk access
# 4. Stable performance O(log n)
```

---

## 4. Searching Algorithms

### 📖 What are Searching Algorithms?

**Searching Algorithms** are techniques for finding a specific element or value within a data structure. The choice of algorithm depends on whether the data is sorted and the data structure used.

**Key Concepts:**

- **Linear Search**: Check each element sequentially - O(n)
- **Binary Search**: Divide and conquer on sorted data - O(log n)
- **Search Space**: The range of possible candidates being searched

**Why is this important for Data Engineering?**

- Binary search is used in database query optimization
- Understanding search algorithms helps choose data structures
- BFS/DFS are fundamental for graph processing

```python
# Linear Search - O(n)
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Binary Search - O(log n) - requires sorted array
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Binary Search - Recursive
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Find first occurrence
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

---

## 5. Sorting Algorithms

### 📖 What are Sorting Algorithms?

**Sorting Algorithms** arrange elements in a specified order (ascending or descending). The choice depends on data size, whether it's nearly sorted, stability requirements, and memory constraints.

**Key Concepts:**

| Algorithm | Best | Average | Worst | Stable | In-Place |
|-----------|------|---------|-------|--------|----------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | Yes | Yes |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | Yes | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | No | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | Yes | No |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | No | Yes |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | No | Yes |
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | Yes | No |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | Yes | No |

**Why is this important for Data Engineering?**

- Sorting is fundamental to many algorithms (binary search requires sorted data)
- Understanding stability matters for multi-key sorting
- Knowing when to use non-comparison sorts (counting, radix) for integers

```python
# Bubble Sort - O(n²), stable, in-place
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Early exit if sorted
            break

# Insertion Sort - O(n²), stable, in-place (good for nearly sorted data)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Selection Sort - O(n²), not stable, in-place
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Merge Sort - O(n log n), stable, not in-place
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort - O(n log n) average, in-place
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Heap Sort - O(n log n), not stable, in-place
def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Counting Sort - O(n + k), stable, for integers
def counting_sort(arr, max_val):
    count = [0] * (max_val + 1)

    for val in arr:
        count[val] += 1

    result = []
    for i, c in enumerate(count):
        result.extend([i] * c)

    return result
```

---

## 6. Graph Algorithms

### 📖 What are Graph Algorithms?

**Graph Algorithms** solve problems on graph structures including finding paths, connectivity, and optimal routes.

**Key Concepts:**

- **Graph Representation**: Adjacency list (space-efficient) vs adjacency matrix (faster lookups)
- **Traversal**: BFS (shortest path in unweighted) vs DFS (path finding, cycle detection)
- **Shortest Path**: Dijkstra (non-negative weights), Bellman-Ford (negative weights), Floyd-Warshall (all pairs)
- **Topological Sort**: Ordering for DAGs (dependency resolution)
- **MST**: Kruskal and Prim for minimum spanning tree

**Why is this important for Data Engineering?**

- Social network analysis
- Route optimization and logistics
- Dependency resolution in build systems
- Database query optimization

```python
from collections import defaultdict, deque
import heapq

# Dijkstra's Algorithm - O((V + E) log V)
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    parent = {}

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current == end:
            break

        if current_dist > distances[current]:
            continue

        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct path
    path = []
    current = end
    while current in parent:
        path.append(current)
        current = parent[current]
    path.append(start)
    return distances[end], path[::-1]

# Bellman-Ford - O(VE), handles negative weights
def bellman_ford(edges, n, start):
    distances = [float('inf')] * n
    distances[start] = 0

    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Check for negative cycles
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return None  # Negative cycle

    return distances

# Topological Sort - O(V + E)
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(graph) else None  # Cycle exists

# Union-Find for Kruskal's MST
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
```

---

## 7. Dynamic Programming

### 📖 What is Dynamic Programming?

**Dynamic Programming (DP)** is an optimization technique that solves complex problems by breaking them into overlapping subproblems. It applies when problems have optimal substructure and overlapping subproblems.

**Key Concepts:**

- **Optimal Substructure**: Solution can be built from optimal solutions of subproblems
- **Overlapping Subproblems**: Same subproblems solved multiple times
- **Memoization (Top-Down)**: Recursive with caching
- **Tabulation (Bottom-Up)**: Iterative, fill table from base cases

**DP Patterns:**

- **1D DP**: Fibonacci, Climbing Stairs, House Robber
- **2D DP**: Grid paths, LCS, Edit Distance
- **Greedy DP**: Coin Change (can be greedy if coins allow)

**Why is this important for Data Engineering?**

- Sequence alignment in bioinformatics
- Resource allocation problems
- String matching algorithms
- Optimization in scheduling

```python
# Fibonacci - Multiple approaches

# Naive recursion - O(2^n)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Memoization (Top-Down) - O(n)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Tabulation (Bottom-Up) - O(n), O(1) space
def fib_tab(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1

# 0/1 Knapsack - O(nW) where W is capacity
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Longest Common Subsequence (LCS) - O(mn)
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Longest Increasing Subsequence (LIS) - O(n log n)
def lis(nums):
    if not nums:
        return 0

    # Binary search approach
    def binary_search(subseq, val):
        left, right = 0, len(subseq)
        while left < right:
            mid = (left + right) // 2
            if subseq[mid] < val:
                left = mid + 1
            else:
                right = mid
        return left

    subseq = []
    for val in nums:
        pos = binary_search(subseq, val)
        if pos == len(subseq):
            subseq.append(val)
        else:
            subseq[pos] = val

    return len(subseq)

# Coin Change - O(amount * len(coins))
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1

    return dp[amount] if dp[amount] != float('inf') else -1

# House Robber - O(n)
def house_robber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, nums[0]

    for i in range(1, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = curr

    return prev1
```

---

## 8. Recursion & Backtracking

### 📖 What are Recursion & Backtracking?

**Recursion** is a technique where a function calls itself to solve smaller instances of the problem. **Backtracking** is an algorithmic technique that tries partial solutions, abandons them when they can't lead to a solution, and tries other possibilities.

**Key Concepts:**

- **Base Case**: Condition that stops recursion
- **Recursive Case**: Problem reduced to smaller subproblems
- **Call Stack**: Each recursive call adds a stack frame
- **Backtracking**: Explore all possibilities, undo choices

**Why is this important for Data Engineering?**

- Tree/graph traversal
- Permutation/combination generation
- Puzzle solving (Sudoku, N-Queens)
- Search algorithms

```python
# Basic Recursion

# Factorial - O(n)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Sum of array - O(n)
def sum_array(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 0:
        return 0
    return arr[n - 1] + sum_array(arr, n - 1)

# Reverse string - O(n)
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

# Backtracking

# Generate all permutations
def permutations(arr):
    result = []

    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return

        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]  # Undo

    backtrack(0)
    return result

# N-Queens - Place N queens on N×N board
def solve_n_queens(n):
    result = []
    board = [-1] * n  # board[i] = column of queen in row i

    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            result.append(["." * col + "Q" + "." * (n - col - 1)
                          for col in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Undo

    backtrack(0)
    return result

# Subsets - Generate all subsets
def subsets(nums):
    result = []

    def backtrack(index, current):
        result.append(current[:])

        for i in range(index, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result

# Combination Sum
def combination_sum(candidates, target):
    result = []

    def backtrack(start, target, current):
        if target == 0:
            result.append(current[:])
            return
        if target < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, target - candidates[i], current)
            current.pop()

    backtrack(0, target, [])
    return result
```

---

## 9. Greedy Algorithms

### 📖 What are Greedy Algorithms?

**Greedy Algorithms** make locally optimal choices at each step, hoping to find a global optimum. They work when the problem has the "greedy choice property" - making the best local choice leads to the best global solution.

**Key Concepts:**

- **Greedy Choice Property**: Local optimal choice leads to global optimal
- **Optimal Substructure**: Problem can be solved by combining optimal solutions
- **No Backtracking**: Decisions are made once and never reconsidered

**Why is this important for Data Engineering?**

- Task scheduling and resource allocation
- Network routing protocols
- Compression (Huffman coding)
- Interval scheduling

```python
# Activity Selection - O(n log n)
def activity_selection(activities):
    # Sort by finish time
    activities.sort(key=lambda x: x[1])

    result = [activities[0]]
    last_finish = activities[0][1]

    for start, end in activities[1:]:
        if start >= last_finish:
            result.append((start, end))
            last_finish = end

    return result

# Fractional Knapsack - O(n log n)
def fractional_knapsack(items, capacity):
    # Sort by value/weight ratio
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    remaining = capacity

    for value, weight in items:
        if remaining == 0:
            break

        if weight <= remaining:
            total_value += value
            remaining -= weight
        else:
            total_value += value * (remaining / weight)
            remaining = 0

    return total_value

# Huffman Coding - O(n log n)
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(text):
    if not text:
        return {}

    # Build frequency table
    freq = Counter(text)

    # Build min heap
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Generate codes
    codes = {}

    def generate_codes(node, current_code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = current_code
            return

        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(heap[0], "")
    return codes

# Minimum Coins (Greedy - works for specific coin systems)
def min_coins_greedy(coins, amount):
    coins = sorted(coins, reverse=True)
    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin

    return count if amount == 0 else -1
```

---

## 10. Complexity Analysis

### 📖 What is Complexity Analysis?

**Complexity Analysis** is the study of algorithm efficiency in terms of time and space resources. It helps predict how algorithms will perform as input size grows.

**Key Concepts:**

- **Big O (O)**: Upper bound (worst case)
- **Big Omega (Ω)**: Lower bound (best case)
- **Big Theta (Θ)**: Tight bound (average case)
- **Space Complexity**: Memory usage

**Common Complexities:**

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Array index access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2^n) | Exponential | Recursive Fibonacci |
| O(n!) | Factorial | Permutations |

**Why is this important for Data Engineering?**

- Predicting pipeline performance
- Choosing algorithms for large datasets
- Resource planning and optimization

```python
# Time complexity examples

# O(1) - Constant
def get_first(arr):
    return arr[0]

# O(n) - Linear
def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = return val
    return max_val

# O(n²) - Quadratic
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(log n) - Logarithmic
def binary_search_example(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n log n) - Linearithmic
def merge_sort_example(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_example(arr[:mid])
    right = merge_sort_example(arr[mid:])
    # ... merge logic

# Space complexity

# O(1) - Constant space
def sum_array(arr):
    total = 0  # Single variable
    for val in arr:
        total += val
    return total

# O(n) - Linear space
def create_copy(arr):
    return arr[:]  # New array of same size

# O(log n) - Logarithmic space (recursion stack)
def binary_search_rec(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, right)
    else:
        return binary_search_rec(arr, target, left, mid - 1)
```

---

## 11. Problem Solving Patterns

### 📖 What are Problem Solving Patterns?

**Problem Solving Patterns** are recurring solution templates that apply to many algorithm problems. Recognizing these patterns helps you quickly identify the right approach.

**Common Patterns:**

| Pattern | Use Case | Key Technique |
|---------|----------|---------------|
| Two Pointers | Sorted arrays, palindromes | Start/end pointers |
| Sliding Window | Subarrays/substrings | Fixed/variable window |
| Fast & Slow | Cycle detection | Runner technique |
| Merge Intervals | Overlapping intervals | Sort + merge |
| Cyclic Sort | Range 1 to n | Index-based placement |
| BFS/DFS | Tree/graph traversal | Queue/stack |
| Top K | K largest/smallest | Heap or quickselect |
| K-way Merge | Sorted lists | Priority queue |

**Why is this important for Data Engineering?**

- Efficient data processing pipelines
- Stream aggregation
- Data validation and cleaning

```python
# Two Pointers
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Sliding Window
def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

def min_subarray_len(target, nums):
    min_len = float('inf')
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

# Fast & Slow Pointers
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Merge Intervals
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged

# Cyclic Sort
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    return nums

# Top K Elements
import heapq

def top_k_heap(nums, k):
    return heapq.nlargest(k, nums)

def top_k_quick(nums, k):
    # Quickselect - O(n) average
    def partition(left, right, pivot):
        pivot_val = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        store = left

        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1

        nums[right], nums[store] = nums[store], nums[right]
        return store

    def select(left, right, k):
        if left == right:
            return left

        pivot = random.randint(left, right)
        pivot = partition(left, right, pivot)

        if k == pivot:
            return k
        elif k < pivot:
            return select(left, pivot - 1, k)
        else:
            return select(pivot + 1, right, k)

    select(0, len(nums) - 1, len(nums) - k)
    return sorted(nums, reverse=True)[:k]

# K-way Merge
def merge_k_sorted(lists):
    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap,
                          (lists[list_idx][elem_idx + 1],
                           list_idx,
                           elem_idx + 1))

    return result
```

---

## 12. Python Implementation Focus

### 📖 What are Python Implementation Focus Areas?

Understanding Python's built-in data structures and libraries helps write efficient code for data engineering tasks.

**Key Python Structures:**

- **list**: Dynamic array, O(1) append, O(n) insert/delete at beginning
- **collections.deque**: Double-ended queue, O(1) for both ends
- **heapq**: Min-heap implementation
- **collections.defaultdict**: Dictionary with default values
- **collections.Counter**: Count hashable objects

**Why is this important for Data Engineering?**

- Efficient data manipulation
- Reducing boilerplate code
- Performance optimization

```python
# Using Lists as Stacks/Queues
stack = []
stack.append(1)    # push - O(1)
stack.pop()       # pop - O(1)

queue = []
queue.append(1)   # enqueue - O(1)
queue.pop(0)      # dequeue - O(n) - inefficient!

# Use deque for efficient queue
from collections import deque
queue = deque()
queue.append(1)   # enqueue - O(1)
queue.popleft()  # dequeue - O(1)

# collections.deque
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)           # right side - O(1)
dq.appendleft(0)       # left side - O(1)
dq.pop()              # right side - O(1)
dq.popleft()          # left side - O(1)

# maxlen for fixed-size deque (circular buffer)
window = deque(maxlen=3)
window.extend([1, 2, 3])
window.append(4)  # Automatically removes oldest (1)

# heapq module
import heapq

# Min heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappop(heap)  # Returns 2

# Max heap (negate values)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
-heapq.heappop(max_heap)  # Returns 5

# Heap sort
arr = [5, 2, 8, 1, 9]
heapq.heapify(arr)  # O(n)
sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]

# nlargest/nsmallest - O(n log k)
import heapq
data = [1, 5, 2, 8, 1, 9, 3, 7]
top_3 = heapq.nlargest(3, data)  # [9, 8, 7]
bottom_3 = heapq.nsmallest(3, data)  # [1, 1, 2]

# collections.defaultdict
from collections import defaultdict

# Automatic default values
dd = defaultdict(int)
dd["a"] += 1  # Creates "a": 1 automatically

# Grouping example
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
by_first = defaultdict(list)
for word in words:
    by_first[word[0]].append(word)
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

# Adjacency list
graph = defaultdict(list)
graph["A"].append("B")
graph["A"].append("C")

# collections.Counter
from collections import Counter

# Count elements
cnt = Counter(["a", "b", "c", "a", "b", "a"])
print(cnt)  # Counter({'a': 3, 'b': 2, 'c': 1})

# Most common
print(cnt.most_common(2))  # [('a', 3), ('b', 2)]

# Operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)       # Counter({'a': 4, 'b': 3})
print(c1 - c2)       # Counter({'a': 2})
print(c1 & c2)       # Intersection: Counter({'a': 1, 'b': 1})
print(c1 | c2)       # Union: Counter({'a': 3, 'b': 2})

# Word frequency in text
text = "hello world hello python world python"
word_count = Counter(text.split())
print(word_count.most_common(1))  # [('hello', 2)]

# Additional useful structures

# namedtuple - Lightweight objects
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)  # 3 4

# OrderedDict - Remembers insertion order (Python 3.7+ dict does too)
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od.move_to_end('a')  # Move to end

# Tips for efficient Python
# 1. Use list comprehension over loops
# 2. Use set for membership testing (O(1) vs O(n))
# 3. Use dict comprehension for simple transforms
# 4. Prefer built-in functions (sum, max, min) over loops
# 5. Use enumerate instead of range(len())
# 6. Use f-strings for formatting (fastest)
```

---

## Quick Reference

### Complexity Cheat Sheet

| Operation | List | Dict | Set | Heap |
|-----------|------|------|-----|------|
| Access | O(1) | O(1) | N/A | N/A |
| Search | O(n) | O(1) | O(1) | O(1) |
| Insert | O(1)* | O(1) | O(1) | O(log n) |
| Delete | O(n) | O(1) | O(1) | O(log n) |

*Amortized

### When to Use What

| Problem Type | Recommended Approach |
|--------------|---------------------|
| Sorted array search | Binary search |
| Top K elements | Heap (nlargest) or Quickselect |
| Prefix matching | Trie |
| Shortest path (weighted) | Dijkstra's |
| Shortest path (unweighted) | BFS |
| Dependency resolution | Topological sort |
| Minimum spanning tree | Kruskal's or Prim's |
| Sequence alignment | Dynamic programming |
| Permutations/combinations | Backtracking |

---

**Happy Learning! Remember: Practice makes perfect.**
