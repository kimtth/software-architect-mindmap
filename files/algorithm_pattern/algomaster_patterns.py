"""
This file contains sample code implementations for common algorithm patterns.
Each pattern includes 2-3 working examples to demonstrate the approach.

https://blog.algomaster.io/p/15-leetcode-patterns

1. Prefix Sum: Precomputes cumulative sums up to each index of an array, allowing for efficient range sum queries.
2. Two Pointers: Utilizes two pointers to traverse data structures, optimizing problems involving pairs in sorted arrays or linked lists.
3. Sliding Window: Maintains a window of elements, slides over it, and updates the result, useful for finding subarrays or substrings that meet specific conditions.
4. Fast & Slow Pointers: Moves two pointers at different speeds to detect cycles in linked lists or arrays and find middle elements.
5. LinkedList In-place Reversal: Reverses a linked list or its parts without extra space, modifying the list in-place.
6. Monotonic Stack: Maintains a stack in increasing or decreasing order of elements, aiding in solving problems involving next/previous greater/smaller elements.
7. Top 'K' Elements: Uses a heap to keep track of the top 'K' elements, efficient for problems requiring frequent retrieval of the largest or smallest elements.
8. Overlapping Intervals: Identifies and manages overlapping intervals, essential for interval scheduling and merging problems.
9. Modified Binary Search: Applies binary search with modifications to solve problems like finding the first or last occurrence of an element.
10. Binary Tree Traversal: Employs depth-first and breadth-first search techniques to traverse binary trees.
11. Depth-First Search (DFS): Explores all nodes of a graph or tree by going as deep as possible before backtracking.
12. Breadth-First Search (BFS): Explores all nodes level by level, suitable for finding the shortest path in unweighted graphs.
13. Matrix Traversal: Navigates through a matrix to solve problems like searching for elements or finding paths.
14. Backtracking: Systematically searches through all possible configurations to solve constraint satisfaction problems.
15. Dynamic Programming Patterns: Breaks down problems into simpler subproblems and solves them just once, storing the solutions for future reference.
"""

# 1. PREFIX SUM PATTERN
print("\n1. PREFIX SUM PATTERN\n" + "-" * 50)

def prefix_sum_array(arr):
    """
    Example 1: Creates a prefix sum array where each element is the sum of all previous elements including itself.
    Time Complexity: O(n), Space Complexity: O(n)
    """
    n = len(arr)
    # Initialize prefix sum array with the same length as input array
    prefix = [0] * n
    # First element remains the same
    prefix[0] = arr[0]
    
    # Calculate prefix sum for each position
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]  # Each value is sum of previous prefix sum and current element
    
    return prefix

# Example usage
arr = [1, 2, 3, 4, 5]
prefix = prefix_sum_array(arr)
print(f"Original array: {arr}")
print(f"Prefix sum array: {prefix}")
# Expected output: Prefix sum array: [1, 3, 6, 10, 15]

def range_sum_query(arr, queries):
    """
    Example 2: Using prefix sum to efficiently answer range sum queries
    Time Complexity: O(n + q), where n is array length and q is number of queries
    Space Complexity: O(n)
    """
    # Build prefix sum array once
    prefix = prefix_sum_array(arr)
    results = []
    
    for start, end in queries:
        if start == 0:
            # If start is 0, the sum is simply the prefix sum at the end index
            results.append(prefix[end])
        else:
            # Otherwise, subtract the prefix sum before start from the prefix sum at end
            results.append(prefix[end] - prefix[start-1])
    
    return results

# Example usage
queries = [(1, 3), (0, 2), (2, 4)]
results = range_sum_query(arr, queries)
print(f"Range sum queries {queries}:")
print(f"Query results: {results}")
# Expected output: Query results: [9, 6, 12]


# 2. TWO POINTERS PATTERN
print("\n2. TWO POINTERS PATTERN\n" + "-" * 50)

def two_sum_sorted(arr, target):
    """
    Example 1: Find two numbers in a sorted array that add up to a target
    Time Complexity: O(n), Space Complexity: O(1)
    """
    left = 0  # Left pointer starts at the beginning
    right = len(arr) - 1  # Right pointer starts at the end
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            # Found the pair
            return [left, right]
        elif current_sum < target:
            # Sum is too small, move left pointer to increase sum
            left += 1
        else:
            # Sum is too large, move right pointer to decrease sum
            right -= 1
    
    return [-1, -1]  # No pair found

# Example usage
sorted_arr = [1, 3, 4, 5, 7, 11]
target = 9
indices = two_sum_sorted(sorted_arr, target)
print(f"Array: {sorted_arr}, Target: {target}")
print(f"Indices of two numbers that sum to target: {indices}")
# Expected output: Indices of two numbers that sum to target: [1, 4]

def remove_duplicates(arr):
    """
    Example 2: Remove duplicates from a sorted array in-place
    Time Complexity: O(n), Space Complexity: O(1)
    """
    if not arr:
        return 0
    
    # Slow pointer represents the position where unique element should be placed
    slow = 0
    
    # Fast pointer scans through the array
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            # Found a new unique element
            slow += 1
            # Place it at the next position in the result
            arr[slow] = arr[fast]
    
    # Return the length of the array without duplicates
    return slow + 1

# Example usage
dup_arr = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5]
length = remove_duplicates(dup_arr)
print(f"Original array: {dup_arr}")
print(f"Array after removing duplicates (first {length} elements): {dup_arr[:length]}")
# Expected output: Array after removing duplicates (first 5 elements): [1, 2, 3, 4, 5]


# 3. SLIDING WINDOW PATTERN
print("\n3. SLIDING WINDOW PATTERN\n" + "-" * 50)

def max_sum_subarray(arr, k):
    """
    Example 1: Find maximum sum subarray of size k
    Time Complexity: O(n), Space Complexity: O(1)
    """
    n = len(arr)
    
    # Handle edge cases
    if n < k:
        return None
    
    # Calculate sum of first window of size k
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window and update max_sum
    for i in range(k, n):
        # Add the next element and remove the first element of previous window
        window_sum = window_sum + arr[i] - arr[i-k]
        # Update max_sum if current window sum is greater
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
max_sum = max_sum_subarray(arr, k)
print(f"Array: {arr}, k: {k}")
print(f"Maximum sum of subarray of size {k}: {max_sum}")
# Expected output: Maximum sum of subarray of size 3: 9

def longest_substring_with_k_distinct(s, k):
    """
    Example 2: Find the longest substring with at most k distinct characters
    Time Complexity: O(n), Space Complexity: O(k)
    """
    if not s or k == 0:
        return 0
    
    char_frequency = {}  # Dictionary to track character frequency
    max_length = 0
    window_start = 0
    
    # Extend the window
    for window_end in range(len(s)):
        # Add current character to frequency map
        right_char = s[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        
        # Shrink the window if we have more than k distinct characters
        while len(char_frequency) > k:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        
        # Update the maximum length
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length

# Example usage
s = "araaci"
k = 2
length = longest_substring_with_k_distinct(s, k)
print(f"String: {s}, k: {k}")
print(f"Length of the longest substring with at most {k} distinct characters: {length}")
# Expected output: Length of the longest substring with at most 2 distinct characters: 4


# 4. FAST & SLOW POINTERS PATTERN
print("\n4. FAST & SLOW POINTERS PATTERN\n" + "-" * 50)

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)

def create_linked_list(values, cycle_pos=-1):
    """Helper function to create a linked list with an optional cycle"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    cycle_node = None
    
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == cycle_pos:
            cycle_node = current
    
    # Create cycle if specified
    if cycle_pos >= 0 and cycle_node:
        current.next = cycle_node
    
    return head

def print_linked_list(head, limit=10):
    """Helper function to print a linked list with cycle detection"""
    if not head:
        return "Empty list"
    
    result = []
    current = head
    visited = set()
    count = 0
    
    while current and count < limit:
        if current in visited:
            result.append(f"{current.value}(cycle)")
            break
        result.append(str(current.value))
        visited.add(current)
        current = current.next
        count += 1
    
    if count == limit and current:
        result.append("...")
    
    return " -> ".join(result)

def has_cycle(head):
    """
    Example 1: Detect if a linked list has a cycle
    Time Complexity: O(n), Space Complexity: O(1)
    """
    if not head or not head.next:
        return False
    
    # Initialize slow and fast pointers
    slow = head  # Moves one step at a time
    fast = head  # Moves two steps at a time
    
    # If there's a cycle, fast will eventually catch up to slow
    while fast and fast.next:
        slow = slow.next       # Move slow one step
        fast = fast.next.next  # Move fast two steps
        
        if slow == fast:  # If pointers meet, there's a cycle
            return True
    
    # If fast reaches the end, there's no cycle
    return False

# Example usage
head1 = create_linked_list([1, 2, 3, 4, 5])
head2 = create_linked_list([1, 2, 3, 4, 5], cycle_pos=2)  # Creates cycle at position 2 (value 3)

print(f"Linked List 1: {print_linked_list(head1)}")
print(f"Has cycle: {has_cycle(head1)}")
# Expected output: Has cycle: False

print(f"Linked List 2: {print_linked_list(head2)}")
print(f"Has cycle: {has_cycle(head2)}")
# Expected output: Has cycle: True

def find_middle_node(head):
    """
    Example 2: Find the middle node of a linked list
    Time Complexity: O(n), Space Complexity: O(1)
    """
    if not head:
        return None
    
    # Initialize slow and fast pointers at the head
    slow = head  # Moves one step at a time
    fast = head  # Moves two steps at a time
    
    # When fast reaches the end, slow will be at the middle
    while fast and fast.next:
        slow = slow.next       # Move slow one step
        fast = fast.next.next  # Move fast two steps
    
    # Slow is at the middle when fast reaches the end
    return slow

# Example usage
head = create_linked_list([1, 2, 3, 4, 5])
middle = find_middle_node(head)
print(f"Linked List: {print_linked_list(head)}")
print(f"Middle node: {middle}")
# Expected output: Middle node: 3

head_even = create_linked_list([1, 2, 3, 4, 5, 6])
middle_even = find_middle_node(head_even)
print(f"Linked List (even length): {print_linked_list(head_even)}")
print(f"Middle node (second middle for even length): {middle_even}")
# Expected output: Middle node (second middle for even length): 4


# 5. LINKEDLIST IN-PLACE REVERSAL PATTERN
print("\n5. LINKEDLIST IN-PLACE REVERSAL PATTERN\n" + "-" * 50)

def reverse_linked_list(head):
    """
    Example 1: Reverse a linked list in-place
    Time Complexity: O(n), Space Complexity: O(1)
    """
    # Initialize pointers
    prev = None  # Previous node (initially None)
    current = head  # Start with the head node
    
    # Iterate until we reach the end of the list
    while current:
        # Store the next node before changing references
        next_temp = current.next
        
        # Reverse the current node's pointer
        current.next = prev
        
        # Move pointers one position ahead
        prev = current
        current = next_temp
    
    # prev is now the new head of the reversed list
    return prev

# Example usage
head = create_linked_list([1, 2, 3, 4, 5])
print(f"Original linked list: {print_linked_list(head)}")
reversed_head = reverse_linked_list(head)
print(f"Reversed linked list: {print_linked_list(reversed_head)}")
# Expected output: Reversed linked list: 5 -> 4 -> 3 -> 2 -> 1

def reverse_sublist(head, p, q):
    """
    Example 2: Reverse a sublist between positions p and q (1-indexed)
    Time Complexity: O(n), Space Complexity: O(1)
    """
    if not head or p == q:
        return head
    
    # Initialize pointers
    current = head
    prev = None
    position = 1
    
    # Move to position p
    while current and position < p:
        prev = current
        current = current.next
        position += 1
    
    # Save the node before sublist (will connect to reversed sublist's head)
    last_node_before_sublist = prev
    
    # Save the first node of sublist (will be the last node after reversal)
    first_node_of_sublist = current
    
    # Reverse nodes from position p to q
    while current and position <= q:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
        position += 1
    
    # Connect the last node before sublist to the new head of reversed sublist
    if last_node_before_sublist:
        last_node_before_sublist.next = prev
    else:
        # If p was 1, update the head of the entire list
        head = prev
    
    # Connect the last node of reversed sublist to the first node after sublist
    first_node_of_sublist.next = current
    
    return head

# Example usage
head = create_linked_list([1, 2, 3, 4, 5])
print(f"Original linked list: {print_linked_list(head)}")
p, q = 2, 4
sublist_reversed = reverse_sublist(head, p, q)
print(f"Linked list with sublist from position {p} to {q} reversed: {print_linked_list(sublist_reversed)}")
# Expected output: Linked list with sublist from position 2 to 4 reversed: 1 -> 4 -> 3 -> 2 -> 5

# ---------------------------
# Pattern 6: Monotonic Stack
# ---------------------------

print("\n6. MONOTONIC STACK PATTERN\n" + "-" * 50)

def next_greater_elements(nums):
    # Create a list of -1's as default output for each element
    res = [-1] * len(nums)
    # Initialize an empty stack to store indices of elements
    stack = []
    # Iterate over each index and element in nums
    for i, num in enumerate(nums):
        # While the stack is not empty and current number is greater than the number at index stored at top of the stack
        while stack and num > nums[stack[-1]]:
            # Pop the index from the stack
            index = stack.pop()
            # Update the result at that index with the current number as it is the next greater element
            res[index] = num
        # Push the current index onto the stack
        stack.append(i)
    # Return the list containing next greater elements for each number
    return res

def previous_smaller_elements(nums):
    # Create a list of -1's as default output for each element
    res = [-1] * len(nums)
    # Initialize an empty stack to store indices of elements
    stack = []
    # Iterate over each index and element in nums
    for i, num in enumerate(nums):
        # While the stack is not empty and the element at the index on top of the stack is not smaller than current num
        while stack and nums[stack[-1]] >= num:
            # Pop from the stack since current num is smaller than nums[stack[-1]]
            stack.pop()
        # If stack is not empty, the top element is the previous smaller element; otherwise, use -1
        res[i] = nums[stack[-1]] if stack else -1
        # Push the current index onto the stack
        stack.append(i)
    # Return the list of previous smaller elements for each number
    return res

# Example usage for Monotonic Stack:
print("Monotonic Stack Example:")
nums = [2, 1, 2, 4, 3]           # Example list of numbers
print("Original list:", nums)     # Print the original list
print("Next Greater Elements:", next_greater_elements(nums))  # Get next greater elements
print("Previous Smaller Elements:", previous_smaller_elements(nums))  # Get previous smaller elements

# -------------------------------------
# Pattern 7: Top 'K' Elements using Heap
# -------------------------------------

print("\n7. TOP 'K' ELEMENTS PATTERN\n" + "-" * 50)

import heapq  # Import heapq for heap operations

def top_k_largest(nums, k):
    # Use heapq.nlargest to find the k largest elements in nums
    return heapq.nlargest(k, nums)

def top_k_smallest(nums, k):
    # Use heapq.nsmallest to find the k smallest elements in nums
    return heapq.nsmallest(k, nums)

# Example usage for Top 'K' Elements:
print("\nTop 'K' Elements Example:")
nums = [3, 1, 5, 12, 2, 11]  # Example list of numbers
k = 3  # Number of top elements to retrieve
print("Original list:", nums)  # Print the original list
print("Top", k, "largest elements:", top_k_largest(nums, k))  # Get the top k largest elements
print("Top", k, "smallest elements:", top_k_smallest(nums, k))  # Get the top k smallest elements

# ----------------------------------
# Pattern 8: Overlapping Intervals
# ----------------------------------

print("\n8. OVERLAPPING INTERVALS PATTERN\n" + "-" * 50)

def merge_intervals(intervals):
    # If there are no intervals, return an empty list
    if not intervals:
        return []
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    # Initialize merged list with the first interval
    merged = [intervals[0]]
    # Iterate over the remaining intervals
    for current in intervals[1:]:
        # If current interval overlaps with the last interval in merged list
        if current[0] <= merged[-1][1]:
            # Merge intervals by updating the end of the last interval
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            # If no overlap, append the current interval to merged list
            merged.append(current)
    # Return the merged intervals list
    return merged

# Example usage for Overlapping Intervals:
print("\nOverlapping Intervals Example:")
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]  # Example intervals list
print("Original intervals:", intervals)  # Print original intervals
print("Merged intervals:", merge_intervals(intervals))  # Print merged intervals after merging overlaps

# -------------------------------------------
# Pattern 9: Modified Binary Search (First/Last Occurrence)
# -------------------------------------------

print("\n9. MODIFIED BINARY SEARCH PATTERN\n" + "-" * 50)

def find_first_occurrence(arr, target):
    # Initialize left and right pointers for binary search
    left, right = 0, len(arr) - 1
    result = -1  # Initialize result to -1 (not found)
    # Continue while the search window is valid
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        # If target is found at mid
        if arr[mid] == target:
            result = mid  # Record mid as potential first occurrence
            right = mid - 1  # Move left to continue search for first occurrence
        elif arr[mid] < target:
            left = mid + 1  # Target is in right half; update left pointer
        else:
            right = mid - 1  # Target is in left half; update right pointer
    # Return the first occurrence index or -1 if not found
    return result

def find_last_occurrence(arr, target):
    # Initialize left and right pointers for binary search
    left, right = 0, len(arr) - 1
    result = -1  # Initialize result to -1 (not found)
    # Continue while the search window is valid
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        # If target is found at mid
        if arr[mid] == target:
            result = mid  # Record mid as potential last occurrence
            left = mid + 1  # Move right to continue search for last occurrence
        elif arr[mid] < target:
            left = mid + 1  # Target is in right half; update left pointer
        else:
            right = mid - 1  # Target is in left half; update right pointer
    # Return the last occurrence index or -1 if not found
    return result

# Example usage for Modified Binary Search:
print("\nModified Binary Search Example:")
arr = [1, 2, 2, 2, 3, 4, 5]  # Sorted array with duplicates
target = 2  # Element to search for
print("Array:", arr)  # Print the sorted array
print("First occurrence of", target, "at index:", find_first_occurrence(arr, target))  # Find first occurrence
print("Last occurrence of", target, "at index:", find_last_occurrence(arr, target))   # Find last occurrence

# ----------------------------------
# Pattern 10: Binary Tree Traversal
# ----------------------------------

print("\n10. BINARY TREE TRAVERSAL PATTERN\n" + "-" * 50)

class TreeNode:
    # Node class for Binary Tree
    def __init__(self, val):
        self.val = val      # Node's value
        self.left = None    # Left child
        self.right = None   # Right child

def inorder_traversal(root):
    # Return empty list if the node is None
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

def preorder_traversal(root):
    # Return empty list if the node is None
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

def postorder_traversal(root):
    # Return empty list if the node is None
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val] if root else []

def bfs_traversal(root):
    # Perform Breadth-First Search (level order traversal) on the tree
    if not root:
        return []  # Return empty list if tree is empty
    result, queue = [], [root]  # Initialize result list and queue with the root node
    while queue:
        node = queue.pop(0)  # Dequeue the front node
        result.append(node.val)  # Append its value to result list
        if node.left:
            queue.append(node.left)  # Enqueue left child if it exists
        if node.right:
            queue.append(node.right)  # Enqueue right child if it exists
    return result  # Return the BFS order list

# Example usage for Binary Tree Traversal:
print("\nBinary Tree Traversal Example:")
# Build a sample binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5
root = TreeNode(1)         # Create root node with value 1
root.left = TreeNode(2)      # Create left child with value 2
root.right = TreeNode(3)     # Create right child with value 3
root.left.left = TreeNode(4) # Create left child of node 2 with value 4
root.left.right = TreeNode(5)# Create right child of node 2 with value 5
print("Inorder Traversal:", inorder_traversal(root))    # Get inorder traversal
print("Preorder Traversal:", preorder_traversal(root))    # Get preorder traversal
print("Postorder Traversal:", postorder_traversal(root))  # Get postorder traversal
print("BFS Traversal:", bfs_traversal(root))              # Get level order (BFS) traversal

# -------------------------------
# Pattern 11: Depth-First Search (DFS)
# -------------------------------

print("\n11. DEPTH-FIRST SEARCH (DFS) PATTERN\n" + "-" * 50)

def dfs(graph, start, visited=None):
    # Initialize visited set if it is None
    if visited is None:
        visited = set()
    # Mark the current node as visited
    visited.add(start)
    # Iterate over each neighbor of the current node
    for neighbor in graph.get(start, []):
        # If the neighbor has not been visited, recursively call dfs
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    # Return the set of visited nodes
    return visited

# Example usage for DFS on a graph:
print("\nDepth-First Search (DFS) Example:")
graph = {
    'A': ['B', 'C'],  # Neighbors of A
    'B': ['D', 'E'],  # Neighbors of B
    'C': ['F'],       # Neighbors of C
    'D': [],          # D has no neighbors
    'E': ['F'],       # E connects to F
    'F': []           # F has no neighbors
}
print("DFS starting from 'A':", dfs(graph, 'A'))  # Perform DFS starting from node 'A'

# -------------------------------
# Pattern 12: Breadth-First Search (BFS)
# -------------------------------

print("\n12. BREADTH-FIRST SEARCH (BFS) PATTERN\n" + "-" * 50)

from collections import deque  # Import deque for efficient FIFO queue operations

def bfs(graph, start):
    # Initialize visited set to keep track of visited nodes
    visited = set()
    # Initialize a deque as queue with the starting node
    queue = deque([start])
    order = []  # List to record the order of node visits
    # Process nodes until the queue is empty
    while queue:
        node = queue.popleft()  # Dequeue the front element
        if node not in visited:
            visited.add(node)   # Mark the node as visited
            order.append(node)  # Append the node to the traversal order
            # Enqueue all unvisited neighbors of the node
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    # Return the order of nodes visited in BFS
    return order

# Example usage for BFS on a graph:
print("\nBreadth-First Search (BFS) Example:")
graph = {
    'A': ['B', 'C'],  # Neighbors of A
    'B': ['D', 'E'],  # Neighbors of B
    'C': ['F'],       # Neighbors of C
    'D': [],          # D has no neighbors
    'E': ['F'],       # E connects to F
    'F': []           # F has no neighbors
}
print("BFS starting from 'A':", bfs(graph, 'A'))  # Perform BFS starting from node 'A'

# -------------------------------------
# Pattern 13: Matrix Traversal - Search in a Matrix
# -------------------------------------

print("\n13. MATRIX TRAVERSAL PATTERN\n" + "-" * 50)

def search_in_matrix(matrix, target):
    # Iterate over each row index and row in matrix
    for i, row in enumerate(matrix):
        # Iterate over each column index and value in the row
        for j, value in enumerate(row):
            # If the value equals the target, return its (row, column) index
            if value == target:
                return (i, j)
    # If target is not found, return (-1, -1)
    return (-1, -1)

# Example usage for Matrix Traversal:
print("\nMatrix Traversal Example:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]  # Define a sample 3x3 matrix
target = 5  # Element to search for in the matrix
print("Matrix:")
for row in matrix:
    print(row)  # Print each row of the matrix
print("Position of target", target, ":", search_in_matrix(matrix, target))  # Search for the target in the matrix

# -------------------------------------
# Pattern 14: Backtracking - Generate All Subsets
# -------------------------------------

print("\n14. BACKTRACKING PATTERN\n" + "-" * 50)

def generate_subsets(nums):
    # Initialize a list to store all possible subsets
    result = []
    def backtrack(start, path):
        # Append a copy of the current subset (path) to result
        result.append(path.copy())
        # Loop through the numbers starting from 'start' index
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            path.append(nums[i])
            # Recursively build further subsets from the remaining numbers
            backtrack(i + 1, path)
            # Backtrack: remove the last element to try next candidate
            path.pop()
    # Start backtracking with an empty path
    backtrack(0, [])
    # Return the list of all subsets
    return result

# Example usage for Backtracking:
print("\nBacktracking Example:")
nums = [1, 2, 3]  # Define a sample list of numbers
print("All subsets of", nums, ":", generate_subsets(nums))  # Generate and print all subsets

# -------------------------------------
# Pattern 15: Dynamic Programming Patterns
# -------------------------------------

print("\n15. DYNAMIC PROGRAMMING PATTERNS\n" + "-" * 50)

# Example 1: Fibonacci using memoization
def fib(n, memo=None):
    # Initialize memo dictionary if it is not provided
    if memo is None:
        memo = {}
    # If n is already computed, return the stored value
    if n in memo:
        return memo[n]
    # Base cases: return n if n is 0 or 1
    if n <= 1:
        return n
    # Compute Fibonacci number recursively with memoization
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    # Return the computed Fibonacci number
    return memo[n]

# Example usage for Fibonacci DP:
print("\nDynamic Programming Example: Fibonacci")
n = 10  # Calculate the 10th Fibonacci number
print("Fibonacci number for", n, ":", fib(n))  # Print Fibonacci number for n

# Example 2: Coin Change Problem using Dynamic Programming
def coin_change(coins, amount):
    # Initialize dp array with infinite values for all amounts from 0 to amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    # Iterate over each amount from 1 to target amount
    for a in range(1, amount + 1):
        # For each coin, check if it can be used to form the current amount
        for coin in coins:
            if coin <= a:
                # Update dp[a] with the minimum coins needed by comparing current value with new computed value
                dp[a] = min(dp[a], dp[a - coin] + 1)
    # If the amount cannot be formed, return -1; otherwise, return dp[amount]
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage for Coin Change DP:
print("\nDynamic Programming Example: Coin Change")
coins = [1, 2, 5]  # Available coin denominations
amount = 11  # Target amount to form
print("Minimum coins required for amount", amount, ":", coin_change(coins, amount))  # Print the minimum coins needed


