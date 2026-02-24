# Data Structures & Algorithms Practice Exercises

Practice your DSA skills with these exercises.

---

## Setup - Python Environment

```python
# Import required modules
from collections import deque, defaultdict, Counter
import heapq
```

---

## Exercise Set 1: Arrays & Strings

### Exercise 1.1: Find Maximum Element
Find the maximum element in an array.

```python
# YOUR CODE HERE:
arr = [3, 1, 4, 1, 5, 9, 2, 6]
# Return the maximum value
```

### Exercise 1.2: Reverse Array
Reverse an array in-place.

```python
# YOUR CODE HERE:
arr = [1, 2, 3, 4, 5]
# Reverse the array
```

### Exercise 1.3: Find Pair with Sum
Find two numbers that add up to a target in a sorted array (Two Pointers).

```python
# YOUR CODE HERE:
def two_sum(arr, target):
    # Use two pointers approach
    pass
```

### Exercise 1.4: Remove Duplicates
Remove duplicates from a sorted array.

```python
# YOUR CODE HERE:
def remove_duplicates(arr):
    # Return new length
    pass
```

### Exercise 1.5: Max Subarray Sum
Find maximum sum of subarray using Sliding Window.

```python
# YOUR CODE HERE:
def max_subarray_sum(arr, k):
    # Use sliding window
    pass
```

---

## Exercise Set 1B: More Arrays (16 Exercises)

### Exercise 1.6: Find Minimum in Rotated Array
Find minimum element in rotated sorted array.

```python
# YOUR CODE HERE:
def find_min(nums):
    # Array is rotated sorted, find minimum
    # nums = [4, 5, 6, 7, 0, 1, 2]
    pass
```

### Exercise 1.7: Search in Rotated Array
Search for target in rotated sorted array.

```python
# YOUR CODE HERE:
def search_rotated(nums, target):
    # Return index or -1
    pass
```

### Exercise 1.8: Container With Most Water
Find container that holds most water.

```python
# YOUR CODE HERE:
def max_area(height):
    # height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    pass
```

### Exercise 1.9: Product of Array Except Self
Calculate product of array except self.

```python
# YOUR CODE HERE:
def product_except_self(nums):
    # Return array where each element is product of all others
    # Cannot use division
    pass
```

### Exercise 1.10: Find Duplicate Number
Find the duplicate number in array [1, n].

```python
# YOUR CODE HERE:
def find_duplicate(nums):
    # nums contains n+1 numbers from 1 to n
    pass
```

### Exercise 1.11: Missing Number
Find missing number from 0 to n.

```python
# YOUR CODE HERE:
def missing_number(nums):
    # All numbers from 0 to n except one
    pass
```

### Exercise 1.12: Rotate Array
Rotate array to the right by k steps.

```python
# YOUR CODE HERE:
def rotate_array(nums, k):
    # Do it in-place
    pass
```

### Exercise 1.13: Move Zeroes
Move all zeroes to end while maintaining order.

```python
# YOUR CODE HERE:
def move_zeroes(nums):
    # Do it in-place
    pass
```

### Exercise 1.14: Third Maximum Number
Find third distinct maximum number.

```python
# YOUR CODE HERE:
def third_max(nums):
    # Return third max or max if less than 3
    pass
```

### Exercise 1.15: Array Partition
Pair array elements to maximize sum.

```python
# YOUR CODE HERE:
def array_pair_sum(nums):
    # Return max sum of pairs
    pass
```

### Exercise 1.16: Subarray Sum Equals K
Count number of continuous subarrays with sum k.

```python
# YOUR CODE HERE:
def subarray_sum(nums, k):
    # Return count
    pass
```

### Exercise 1.17: Find All Duplicates
Find all duplicate numbers in array.

```python
# YOUR CODE HERE:
def find_all_duplicates(nums):
    # Return list of duplicates
    pass
```

### Exercise 1.18: Plus One
Add one to large integer represented as array.

```python
# YOUR CODE HERE:
def plus_one(digits):
    # digits = [1, 2, 3]
    pass
```

### Exercise 1.19: Merge Sorted Arrays
Merge two sorted arrays into one sorted array.

```python
# YOUR CODE HERE:
def merge_sorted(nums1, m, nums2, n):
    # Merge in-place
    pass
```

### Exercise 1.20: Squares of Sorted Array
Return squares of sorted array in sorted order.

```python
# YOUR CODE HERE:
def sorted_squares(nums):
    # nums is sorted, return squares sorted
    pass
```

### Exercise 1.21: Longest Subarray with Sum K
Find longest subarray with sum equals k.

```python
# YOUR CODE HERE:
def longest_subarray(nums, k):
    # Return length
    pass
```

---

## Exercise Set 1C: Strings (18 Exercises)

### Exercise 1.22: Reverse String
Reverse a string in-place.

```python
# YOUR CODE HERE:
def reverse_string(s):
    # Reverse in-place, s is list of characters
    pass
```

### Exercise 1.23: Valid Palindrome
Check if string is palindrome (alphanumeric only).

```python
# YOUR CODE HERE:
def is_palindrome(s):
    # "A man, a plan, a canal: Panama" -> True
    pass
```

### Exercise 1.24: Longest Substring Without Repeating
Find length of longest substring without repeating chars.

```python
# YOUR CODE HERE:
def length_of_longest_substring(s):
    # s = "abcabcbb"
    pass
```

### Exercise 1.25: Longest Repeating Character
Find longest repeating character replacement.

```python
# YOUR CODE HERE:
def character_replacement(s, k):
    # Replace k chars to make all same
    pass
```

### Exercise 1.26: Minimum Window Substring
Find minimum window containing all characters.

```python
# YOUR CODE HERE:
def min_window(s, t):
    # s = "ADOBECODEBANC", t = "ABC"
    pass
```

### Exercise 1.27: Valid Anagram
Check if two strings are anagrams.

```python
# YOUR CODE HERE:
def is_anagram(s, t):
    pass
```

### Exercise 1.28: Group Anagrams
Group anagrams together.

```python
# YOUR CODE HERE:
def group_anagrams(strs):
    # Return grouped result
    pass
```

### Exercise 1.29: Valid Parentheses
Check if parentheses are valid.

```python
# YOUR CODE HERE:
def is_valid(s):
    # s = "()[]{}"
    pass
```

### Exercise 1.30: Longest Common Prefix
Find longest common prefix among strings.

```python
# YOUR CODE HERE:
def longest_common_prefix(strs):
    # ["flower", "flow", "flight"]
    pass
```

### Exercise 1.31: Reverse Words in String
Reverse words in a string.

```python
# YOUR CODE HERE:
def reverse_words(s):
    # "the sky is blue" -> "blue is sky the"
    pass
```

### Exercise 1.32: String to Integer (atoi)
Implement atoi function.

```python
# YOUR CODE HERE:
def my_atoi(s):
    # Convert string to integer
    pass
```

### Exercise 1.33: Count and Say
Return nth count-and-say sequence.

```python
# YOUR CODE HERE:
def count_and_say(n):
    # n = 4 -> "1211"
    pass
```

### Exercise 1.34: First Unique Character
Find first unique character in string.

```python
# YOUR CODE HERE:
def first_unique_char(s):
    # Return index or -1
    pass
```

### Exercise 1.35: Isomorphic Strings
Check if two strings are isomorphic.

```python
# YOUR CODE HERE:
def is_isomorphic(s, t):
    # "egg" -> "add" = True
    pass
```

### Exercise 1.36: Palindromic Substrings
Count palindromic substrings.

```python
# YOUR CODE HERE:
def count_substrings(s):
    # "abc" -> 3, "aaa" -> 6
    pass
```

### Exercise 1.37: Decode String
Decode encoded string.

```python
# YOUR CODE HERE:
def decode_string(s):
    # s = "3[a2[c]]" -> "accaccacc"
    pass
```

### Exercise 1.38: Excel Sheet Column Number
Convert column title to number.

```python
# YOUR CODE HERE:
def title_to_number(s):
    # "A" -> 1, "AB" -> 28
    pass
```

### Exercise 1.39: Common Prefix
Check if strings have common prefix of length k.

```python
# YOUR CODE HERE:
def has_common_prefix(strs, k):
    # Return True if common prefix >= k
    pass
```

---

## Exercise Set 2: Linked Lists

### Exercise 2.1: Create Linked List
Implement a singly linked list with insert_at_head.

```python
# YOUR CODE HERE:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_at_head(head, val):
    # Create new node and insert at head
    pass
```

### Exercise 2.2: Reverse Linked List
Reverse a linked list.

```python
# YOUR CODE HERE:
def reverse_list(head):
    # Reverse the linked list
    pass
```

### Exercise 2.3: Find Middle
Find the middle node of a linked list.

```python
# YOUR CODE HERE:
def find_middle(head):
    # Use fast and slow pointers
    pass
```

### Exercise 2.4: Detect Cycle
Detect if linked list has a cycle.

```python
# YOUR CODE HERE:
def has_cycle(head):
    # Use Floyd's cycle detection
    pass
```

---

## Exercise Set 3: Stacks & Queues

### Exercise 3.1: Valid Parentheses
Check if parentheses are balanced.

```python
# YOUR CODE HERE:
def is_valid(s):
    # s = "()[]{}"
    pass
```

### Exercise 3.2: Implement Queue
Implement queue using deque.

```python
# YOUR CODE HERE:
class Queue:
    def __init__(self):
        # Use deque
        pass

    def enqueue(self, val):
        pass

    def dequeue(self):
        pass
```

### Exercise 3.3: Stack using Queue
Implement stack using two queues.

```python
# YOUR CODE HERE:
class MyStack:
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass
```

### Exercise 3.4: Next Greater Element
Find next greater element for each element.

```python
# YOUR CODE HERE:
def next_greater(arr):
    # Use stack
    pass
```

---

## Exercise Set 4: Hash Tables

### Exercise 4.1: Two Sum
Find indices of two numbers that add to target.

```python
# YOUR CODE HERE:
def two_sum(nums, target):
    # Use hash map
    pass
```

### Exercise 4.2: Count Frequency
Count frequency of each element.

```python
# YOUR CODE HERE:
def count_frequency(arr):
    # Use Counter or dict
    pass
```

### Exercise 4.3: Find Unique Elements
Find elements that appear once.

```python
# YOUR CODE HERE:
def find_unique(arr):
    # All others appear twice
    pass
```

### Exercise 4.4: Group Anagrams
Group strings that are anagrams.

```python
# YOUR CODE HERE:
def group_anagrams(strs):
    # Return grouped anagrams
    pass
```

---

## Exercise Set 5: Trees

### Exercise 5.1: Binary Tree Node
Create a binary tree node class.

```python
# YOUR CODE HERE:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        pass
```

### Exercise 5.2: Inorder Traversal
Perform inorder traversal (left, root, right).

```python
# YOUR CODE HERE:
def inorder_traversal(root):
    # Return list of values
    pass
```

### Exercise 5.3: Preorder Traversal
Perform preorder traversal (root, left, right).

```python
# YOUR CODE HERE:
def preorder_traversal(root):
    pass
```

### Exercise 5.4: BFS Level Order
Level order traversal using BFS.

```python
# YOUR CODE HERE:
def level_order(root):
    # Return list of levels
    pass
```

### Exercise 5.5: Find Max Depth
Find maximum depth of binary tree.

```python
# YOUR CODE HERE:
def max_depth(root):
    pass
```

---

## Exercise Set 6: Binary Search

### Exercise 6.1: Binary Search
Implement binary search on sorted array.

```python
# YOUR CODE HERE:
def binary_search(arr, target):
    # Return index or -1
    pass
```

### Exercise 6.2: Find First Occurrence
Find first occurrence of target.

```python
# YOUR CODE HERE:
def find_first(arr, target):
    pass
```

### Exercise 6.3: Search Insert Position
Find where to insert target.

```python
# YOUR CODE HERE:
def search_insert(nums, target):
    pass
```

### Exercise 6.4: Find Square Root
Find integer square root.

```python
# YOUR CODE HERE:
def my_sqrt(x):
    # Use binary search
    pass
```

---

## Exercise Set 7: Sorting

### Exercise 7.1: Bubble Sort
Implement bubble sort.

```python
# YOUR CODE HERE:
def bubble_sort(arr):
    # Sort in-place
    pass
```

### Exercise 7.2: Merge Sort
Implement merge sort.

```python
# YOUR CODE HERE:
def merge_sort(arr):
    # Return sorted array
    pass
```

### Exercise 7.3: Quick Sort
Implement quick sort.

```python
# YOUR CODE HERE:
def quick_sort(arr):
    pass
```

### Exercise 7.4: Find Kth Largest
Find Kth largest element.

```python
# YOUR CODE HERE:
def find_kth_largest(nums, k):
    # Use heap or quickselect
    pass
```

---

## Exercise Set 8: Graph Algorithms

### Exercise 8.1: Create Graph
Create graph using adjacency list.

```python
# YOUR CODE HERE:
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        pass
```

### Exercise 8.2: BFS
Implement BFS traversal.

```python
# YOUR CODE HERE:
def bfs(graph, start):
    # Return visited nodes
    pass
```

### Exercise 8.3: DFS
Implement DFS traversal.

```python
# YOUR CODE HERE:
def dfs(graph, start):
    pass
```

### Exercise 8.4: Number of Islands
Count number of islands in grid.

```python
# YOUR CODE HERE:
def num_islands(grid):
    # grid is 2D array of 0s and 1s
    pass
```

### Exercise 8.5: Topological Sort
Implement topological sort.

```python
# YOUR CODE HERE:
def topological_sort(graph):
    # Return sorted order
    pass
```

---

## Exercise Set 9: Dynamic Programming

### Exercise 9.1: Fibonacci
Implement Fibonacci with memoization.

```python
# YOUR CODE HERE:
def fib(n):
    # Use memoization (top-down)
    pass

def fib_tab(n):
    # Use tabulation (bottom-up)
    pass
```

### Exercise 9.2: Climbing Stairs
Count ways to climb n stairs.

```python
# YOUR CODE HERE:
def climb_stairs(n):
    # Can climb 1 or 2 steps at a time
    pass
```

### Exercise 9.3: Coin Change
Find minimum coins needed.

```python
# YOUR CODE HERE:
def coin_change(coins, amount):
    # Return minimum coins or -1
    pass
```

### Exercise 9.4: Longest Increasing Subsequence
Find LIS length.

```python
# YOUR CODE HERE:
def lis(nums):
    pass
```

### Exercise 9.5: 0/1 Knapsack
Solve knapsack problem.

```python
# YOUR CODE HERE:
def knapsack(weights, values, capacity):
    # Return maximum value
    pass
```

### Exercise 9.6: House Robber
Maximum money to rob.

```python
# YOUR CODE HERE:
def house_robber(nums):
    # Can't rob adjacent houses
    pass
```

---

## Exercise Set 10: Recursion & Backtracking

### Exercise 10.1: Factorial
Calculate factorial using recursion.

```python
# YOUR CODE HERE:
def factorial(n):
    pass
```

### Exercise 10.2: Generate Permutations
Generate all permutations.

```python
# YOUR CODE HERE:
def permutations(arr):
    # Return list of all permutations
    pass
```

### Exercise 10.3: Generate Subsets
Generate all subsets.

```python
# YOUR CODE HERE:
def subsets(nums):
    pass
```

### Exercise 10.4: N-Queens
Solve N-Queens problem.

```python
# YOUR CODE HERE:
def solve_n_queens(n):
    # Return all valid solutions
    pass
```

### Exercise 10.5: Combination Sum
Find all combinations that sum to target.

```python
# YOUR CODE HERE:
def combination_sum(candidates, target):
    pass
```

---

## Exercise Set 11: Greedy Algorithms

### Exercise 11.1: Activity Selection
Select maximum non-overlapping activities.

```python
# YOUR CODE HERE:
def activity_selection(activities):
    # activities = [(start, end), ...]
    pass
```

### Exercise 11.2: Fractional Knapsack
Solve fractional knapsack.

```python
# YOUR CODE HERE:
def fractional_knapsack(items, capacity):
    # items = [(value, weight), ...]
    pass
```

### Exercise 11.3: Huffman Coding
Implement basic Huffman coding.

```python
# YOUR CODE HERE:
def huffman_coding(text):
    # Return codes dictionary
    pass
```

---

## Exercise Set 12: Heaps

### Exercise 12.1: K Largest Elements
Find K largest elements.

```python
# YOUR CODE HERE:
def k_largest(nums, k):
    # Use heap
    pass
```

### Exercise 12.2: Merge K Sorted Lists
Merge K sorted arrays.

```python
# YOUR CODE HERE:
def merge_k_sorted(lists):
    # lists is list of sorted arrays
    pass
```

### Exercise 12.3: Median of Data Stream
Find median from data stream.

```python
# YOUR CODE HERE:
class MedianFinder:
    def __init__(self):
        pass

    def add_num(self, num):
        pass

    def find_median(self):
        pass
```

---

## Challenge Exercises

### Challenge 1: LRU Cache
Implement LRU Cache.

```python
# YOUR CODE HERE:
class LRUCache:
    def __init__(self, capacity):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass
```

### Challenge 2: Word Search
Find word in 2D grid.

```python
# YOUR CODE HERE:
def exist(board, word):
    # Check if word exists in board
    pass
```

### Challenge 3: Serialize/Deserialize Tree
Serialize and deserialize binary tree.

```python
# YOUR CODE HERE:
class Codec:
    def serialize(self, root):
        pass

    def deserialize(self, data):
        pass
```

---

## Testing Your Code

```python
# Test examples
if __name__ == "__main__":
    # Arrays
    print(max_subarray_sum([1, 2, 3, 4, 5], 3))  # 12

    # Hash
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

    # DP
    print(climb_stairs(5))  # 8

    # Binary Search
    print(binary_search([1, 2, 3, 4, 5], 3))  # 2
```

---

## Complexity Reference

| Operation | Time Complexity |
|-----------|----------------|
| Array Access | O(1) |
| Array Search | O(n) |
| Binary Search | O(log n) |
| Insert/Delete at end | O(1) amortized |
| Hash Table | O(1) average |
| Stack/Queue | O(1) push/pop |
| Tree Traversal | O(n) |
| Heap | O(log n) push/pop |

---

## Practice Complete!

After completing these exercises, you should be comfortable with:
- Arrays and string manipulation
- Linked list operations
- Stack and queue implementations
- Hash table problem solving
- Binary tree traversals
- Binary search patterns
- Sorting algorithms
- Graph traversals (BFS/DFS)
- Dynamic programming approaches
- Recursion and backtracking
- Greedy algorithms
- Heap operations
