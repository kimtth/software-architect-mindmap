#####################################
# 🔹 Two Pointers
#####################################


def two_sum_sorted(nums, target):
    """Find pair with given sum in sorted array"""
    left, right = (
        0,
        len(nums) - 1,
    )  # Initialize two pointers: left at the start, right at the end
    while left < right:  # Continue until the two pointers meet
        current_sum = nums[left] + nums[right]  # Calculate the sum of the two elements
        if current_sum == target:  # If the sum matches the target, return the indices
            return [left, right]
        elif (
            current_sum < target
        ):  # If the sum is less than the target, move the left pointer to the right
            left += 1
        else:  # If the sum is greater than the target, move the right pointer to the left
            right -= 1
    return []  # Return an empty list if no pair is found


def remove_duplicates(nums):
    """Remove duplicates from sorted array"""
    if not nums:  # Handle edge case where the input array is empty
        return 0

    slow = 0  # Initialize the slow pointer to track the position of the last unique element. Moves only when a unique element is found.
    for fast in range(1, len(nums)):  # Iterate through the array with the fast pointer (one step per iteration)
        if nums[fast] != nums[slow]:  # If a new unique element is found
            slow += 1  # Move the slow pointer forward
            nums[slow] = nums[fast]  # Update the position of the unique element
    return slow + 1  # Return the count of unique elements (slow pointer + 1)


# Example usage:
print("\n🔹 Two Pointers:")
# Example 1: Find pair with given sum
nums1 = [1, 2, 3, 4, 5]
target1 = 6
print(f"Two Sum Sorted ([1,2,3,4,5], 6): {two_sum_sorted(nums1, target1)}")

# Example 2: Remove duplicates
nums2 = [1, 1, 2, 3, 3, 4, 4, 4, 5]
k = remove_duplicates(nums2.copy())
print(f"Remove Duplicates from [1,1,2,3,3,4,4,4,5]: {k} unique elements")

# Output:
# 🔹 Two Pointers:
# Two Sum Sorted ([1,2,3,4,5], 6): [0, 4]
# Remove Duplicates from [1,1,2,3,3,4,4,4,5]: 5 unique elements


#####################################
# 🔹 Intervals
#####################################


def merge_intervals(intervals):
    """Merge overlapping intervals"""
    if not intervals:  # If the input list is empty, return an empty list
        return []

    intervals.sort(key=lambda x: x[0])  # Sort intervals by their start times
    merged = [intervals[0]]  # Initialize the merged list with the first interval

    for current in intervals[1:]:  # Iterate through the remaining intervals
        prev = merged[-1]  # Get the last interval in the merged list
        if (
            current[0] <= prev[1]
        ):  # Check if the current interval overlaps with the previous one
            prev[1] = max(
                prev[1], current[1]
            )  # Merge the intervals by updating the end time
        else:  # If there is no overlap, add the current interval to the merged list
            merged.append(current)

    return merged  # Return the merged list of intervals


def min_meeting_rooms(intervals):
    """Find minimum number of meeting rooms required"""
    if not intervals:  # If there are no intervals, no meeting rooms are needed
        return 0

    # Separate start and end times from the intervals
    start_times = sorted([i[0] for i in intervals])  # Sort the start times
    end_times = sorted([i[1] for i in intervals])  # Sort the end times

    rooms = 0  # Initialize the count of meeting rooms
    end_ptr = 0  # Pointer to track the earliest ending meeting

    for start in start_times:  # Iterate through each start time
        if (
            start >= end_times[end_ptr]
        ):  # If the current meeting starts after the earliest ending meeting
            end_ptr += 1  # Move the end pointer to the next meeting
        else:  # Otherwise, a new meeting room is needed
            rooms += 1  # Increment the room count

    return rooms  # Return the total number of meeting rooms required


# Example usage:
print("\n🔹 Intervals:")
# Example 1: Merge intervals
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(f"Merge Intervals {intervals1}: {merge_intervals(intervals1)}")

# Example 2: Meeting rooms
intervals2 = [[0, 30], [5, 10], [15, 20]]
print(f"Min Meeting Rooms {intervals2}: {min_meeting_rooms(intervals2)}")

# Output:
# 🔹 Intervals:
# Merge Intervals [[1, 3], [2, 6], [8, 10], [15, 18]]: [[1, 6], [8, 10], [15, 18]]
# Min Meeting Rooms [[0, 30], [5, 10], [15, 20]]: 2


#####################################
# 🔹 Dynamic Programming
#####################################


def fibonacci(n, memo={}):
    """Fibonacci with memoization"""
    if (
        n in memo
    ):  # Check if the result for n is already computed and stored in the memo dictionary
        return memo[n]
    if n <= 1:  # Base case: Fibonacci of 0 is 0, and Fibonacci of 1 is 1
        return n

    # Recursive case: Compute Fibonacci of n using the sum of the two previous Fibonacci numbers
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]  # Return the computed Fibonacci number


def longest_increasing_subsequence(nums):
    """Longest Increasing Subsequence"""
    if not nums:  # Handle edge case where the input list is empty
        return 0

    n = len(nums)  # Get the length of the input list
    dp = [
        1
    ] * n  # Initialize the dp array with 1, as each element is a subsequence of length 1 by itself

    for i in range(1, n):  # Iterate through the list starting from the second element
        for j in range(i):  # Check all previous elements
            if (
                nums[i] > nums[j]
            ):  # If the current element is greater than a previous element
                dp[i] = max(
                    dp[i], dp[j] + 1
                )  # Update dp[i] to the maximum length of subsequence ending at i

    return max(
        dp
    )  # Return the maximum value in the dp array, which is the length of the LIS


# Example usage:
print("\n🔹 Dynamic Programming:")
# Example 1: Fibonacci
n = 10
print(f"Fibonacci({n}): {fibonacci(n)}")

# Example 2: Longest Increasing Subsequence
nums3 = [10, 9, 2, 5, 3, 7, 101, 18]
print(
    f"Longest Increasing Subsequence {nums3}: {longest_increasing_subsequence(nums3)}"
)

# Output:
# 🔹 Dynamic Programming:
# Fibonacci(10): 55
# Longest Increasing Subsequence [10, 9, 2, 5, 3, 7, 101, 18]: 4


#####################################
# 🔹 Tree Traversal
#####################################


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child


def inorder_traversal(root):
    """Recursive inorder traversal"""
    result = []  # Initialize the result list
    if root:  # If the current node is not None
        result.extend(inorder_traversal(root.left))  # Traverse the left subtree
        result.append(root.val)  # Visit the current node
        result.extend(inorder_traversal(root.right))  # Traverse the right subtree
    return result  # Return the result list


def preorder_traversal(root):
    """Recursive preorder traversal"""
    result = []  # Initialize the result list
    if root:  # If the current node is not None
        result.append(root.val)  # Visit the current node
        result.extend(preorder_traversal(root.left))  # Traverse the left subtree
        result.extend(preorder_traversal(root.right))  # Traverse the right subtree
    return result  # Return the result list


def inorder_traversal_iterative(root):
    """Iterative inorder traversal"""
    result = []  # Initialize the result list
    stack = []  # Initialize the stack to simulate recursion
    current = root  # Start with the root node

    while current or stack:  # Continue while there are nodes to process
        # Reach the leftmost node of the current subtree
        while current:
            stack.append(current)  # Push the current node onto the stack
            current = current.left  # Move to the left child

        current = stack.pop()  # Pop the top node from the stack
        result.append(current.val)  # Visit the node

        # Move to the right subtree
        current = current.right

    return result  # Return the result list


# Example usage:
print("\n🔹 Tree Traversal:")
# Create a sample tree:     1
#                         /   \
#                        2     3
#                       / \   / \
#                      4   5 6   7
tree = TreeNode(
    1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
)

# Example 1: Inorder traversal (recursive)
print(f"Inorder Traversal (recursive): {inorder_traversal(tree)}")

# Example 2: Preorder traversal (recursive)
print(f"Preorder Traversal (recursive): {preorder_traversal(tree)}")

# Example 3: Inorder traversal (iterative)
print(f"Inorder Traversal (iterative): {inorder_traversal_iterative(tree)}")

# Output:
# 🔹 Tree Traversal:
# Inorder Traversal (recursive): [4, 2, 5, 1, 6, 3, 7]
# Preorder Traversal (recursive): [1, 2, 4, 5, 3, 6, 7]
# Inorder Traversal (iterative): [4, 2, 5, 1, 6, 3, 7]


#####################################
# 🔹 DFS-BFS
#####################################


def num_islands(grid):
    """DFS on grid (Number of Islands)"""
    if not grid:  # If the grid is empty, return 0
        return 0

    rows, cols = len(grid), len(
        grid[0]
    )  # Get the number of rows and columns in the grid
    count = 0  # Initialize the count of islands to 0

    def dfs(r, c):
        # Base case: If out of bounds or the cell is water ('0'), return
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return

        grid[r][c] = "0"  # Mark the current cell as visited by setting it to '0'

        # Recursively visit all four directions (up, down, left, right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):  # Iterate through each row
        for c in range(cols):  # Iterate through each column
            if grid[r][c] == "1":  # If the cell is land ('1'), it is part of an island
                count += 1  # Increment the island count
                dfs(r, c)  # Perform DFS to mark the entire island as visited

    return count  # Return the total number of islands


from collections import deque


def level_order(root):
    """BFS level order traversal"""
    if not root:  # If the tree is empty, return an empty list
        return []

    result = []  # Initialize the result list to store levels
    queue = deque([root])  # Initialize the queue with the root node

    while queue:  # Continue while there are nodes in the queue
        level_size = len(queue)  # Get the number of nodes at the current level
        level = []  # Initialize a list to store the current level's values

        for _ in range(level_size):  # Process all nodes at the current level
            node = queue.popleft()  # Remove the node from the front of the queue
            level.append(node.val)  # Add the node's value to the current level

            if node.left:  # If the node has a left child, add it to the queue
                queue.append(node.left)
            if node.right:  # If the node has a right child, add it to the queue
                queue.append(node.right)

        result.append(level)  # Add the current level to the result list

    return result  # Return the list of levels


# Example usage:
print("\n🔹 DFS-BFS:")
# Example 1: Number of Islands (DFS)
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(f"Number of Islands: {num_islands([row[:] for row in grid])}")

# Example 2: Level order traversal (BFS)
print(f"Level Order Traversal: {level_order(tree)}")

# Output:
# 🔹 DFS-BFS:
# Number of Islands: 3
# Level Order Traversal: [[1], [2, 3], [4, 5, 6, 7]]


#####################################
# 🔹 Binary Search
#####################################


def binary_search(nums, target):
    """Classic binary search"""
    left, right = (
        0,
        len(nums) - 1,
    )  # Initialize pointers to the start and end of the array

    while left <= right:  # Continue searching while the pointers do not cross
        mid = left + (right - left) // 2  # Calculate the middle index to avoid overflow

        if (
            nums[mid] == target
        ):  # If the middle element matches the target, return its index
            return mid
        elif nums[mid] < target:  # If the middle element is less than the target
            left = mid + 1  # Move the left pointer to the right of mid
        else:  # If the middle element is greater than the target
            right = mid - 1  # Move the right pointer to the left of mid

    return -1  # Return -1 if the target is not found


def search_range(nums, target):
    """Find first and last position of a target in a sorted array"""

    def find_bound(is_first):
        left, right = (
            0,
            len(nums) - 1,
        )  # Initialize pointers to the start and end of the array
        result = -1  # Initialize the result to -1 (not found)

        while left <= right:  # Continue searching while the pointers do not cross
            mid = left + (right - left) // 2  # Calculate the middle index

            if nums[mid] == target:  # If the middle element matches the target
                result = mid  # Update the result with the current index
                if is_first:  # If searching for the first occurrence
                    right = mid - 1  # Narrow the search to the left half
                else:  # If searching for the last occurrence
                    left = mid + 1  # Narrow the search to the right half
            elif nums[mid] < target:  # If the middle element is less than the target
                left = mid + 1  # Move the left pointer to the right of mid
            else:  # If the middle element is greater than the target
                right = mid - 1  # Move the right pointer to the left of mid

        return result  # Return the index of the bound (or -1 if not found)

    # Find the first and last positions of the target
    return [find_bound(True), find_bound(False)]


# Example usage:
print("\n🔹 Binary Search:")
# Example 1: Classic binary search
nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 7
print(f"Binary Search ([1-10], 7): {binary_search(nums4, target2)}")

# Example 2: Find range
nums5 = [5, 7, 7, 8, 8, 8, 10]
target3 = 8
print(f"Search Range {nums5}, target=8: {search_range(nums5, target3)}")

# Output:
# 🔹 Binary Search:
# Binary Search ([1-10], 7): 6
# Search Range [5, 7, 7, 8, 8, 8, 10], target=8: [3, 5]


#####################################
# 🔹 Array
#####################################


def rotate_array(nums, k):
    """Rotate array to the right by k steps"""
    n = len(nums)  # Get the length of the array
    k = k % n  # Handle cases where k is greater than the array length

    def reverse(start, end):
        """Helper function to reverse elements in the array between indices start and end"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]  # Swap elements
            start += 1  # Move the start pointer forward
            end -= 1  # Move the end pointer backward

    # Reverse the entire array
    reverse(0, n - 1)
    # Reverse the first k elements
    reverse(0, k - 1)
    # Reverse the remaining elements
    reverse(k, n - 1)

    return nums  # Return the rotated array


def max_subarray_sum(nums):
    """Kadane's algorithm for maximum subarray sum"""
    if not nums:  # Handle edge case where the input array is empty
        return 0

    max_so_far = current_max = nums[
        0
    ]  # Initialize the maximum sums with the first element

    for num in nums[1:]:  # Iterate through the array starting from the second element
        current_max = max(
            num, current_max + num
        )  # Update the current maximum subarray sum
        max_so_far = max(
            max_so_far, current_max
        )  # Update the global maximum subarray sum

    return max_so_far  # Return the maximum subarray sum


# Example usage:
print("\n🔹 Array:")
# Example 1: Rotate array
nums6 = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(f"Rotate Array {nums6} by k=3: {rotate_array(nums6.copy(), k)}")

# Example 2: Max subarray sum
nums7 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Max Subarray Sum {nums7}: {max_subarray_sum(nums7)}")

# Output:
# 🔹 Array:
# Rotate Array [1, 2, 3, 4, 5, 6, 7] by k=3: [5, 6, 7, 1, 2, 3, 4]
# Max Subarray Sum [-2, 1, -3, 4, -1, 2, 1, -5, 4]: 6


#####################################
# 🔹 Sliding Window
#####################################


def max_sliding_window(nums, k):
    """Find maximum in each sliding window of size k"""
    result = []  # List to store the maximums of each sliding window
    from collections import deque

    dq = deque()  # Deque to store indices of elements in the current window

    for i, num in enumerate(nums):  # Iterate through the array
        # Remove elements outside the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()  # Remove the index of the element that is out of the window

        # Remove smaller elements as they cannot be the maximum
        while dq and nums[dq[-1]] < num:
            dq.pop()  # Remove the index of the smaller element

        dq.append(i)  # Add the current element's index to the deque

        # Add the maximum of the current window to the result
        if (
            i >= k - 1
        ):  # Start adding to the result only when the first window is complete
            result.append(
                nums[dq[0]]
            )  # The element at the front of the deque is the maximum

    return result  # Return the list of maximums for each sliding window


def longest_substring_without_repeating(s):
    """Longest substring without repeating characters"""
    char_dict = {}  # Dictionary to store the last index of each character
    max_length = 0  # Variable to store the maximum length of substring found
    start = 0  # Start index of the current substring

    for i, char in enumerate(s):  # Iterate through the string
        # If the character is already in the substring, update the start index
        if char in char_dict and start <= char_dict[char]:
            start = (
                char_dict[char] + 1
            )  # Move the start index to the right of the last occurrence
        else:
            max_length = max(max_length, i - start + 1)  # Update the maximum length

        char_dict[char] = i  # Update the last index of the current character

    return max_length  # Return the length of the longest substring without repeating characters


# Example usage:
print("\n🔹 Sliding Window:")
# Example 1: Max sliding window
nums8 = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(f"Max Sliding Window {nums8}, k=3: {max_sliding_window(nums8, k)}")

# Example 2: Longest substring without repeating
s = "abcabcbb"
print(
    f"Longest Substring Without Repeating '{s}': {longest_substring_without_repeating(s)}"
)

# Output:
# 🔹 Sliding Window:
# Max Sliding Window [1, 3, -1, -3, 5, 3, 6, 7], k=3: [3, 3, 5, 5, 6, 7]
# Longest Substring Without Repeating 'abcabcbb': 3


#####################################
# 🔹 Backtracking
#####################################


def permute(nums):
    """Generate all permutations"""
    result = []  # List to store all permutations

    def backtrack(start):
        if start == len(nums):  # Base case: All elements are fixed
            result.append(
                nums[:]
            )  # Add a copy of the current permutation to the result
            return

        for i in range(start, len(nums)):  # Iterate through the remaining elements
            nums[start], nums[i] = (
                nums[i],
                nums[start],
            )  # Swap the current element with the start
            backtrack(
                start + 1
            )  # Recurse to generate permutations for the next position
            nums[start], nums[i] = (
                nums[i],
                nums[start],
            )  # Backtrack to restore the original order

    backtrack(0)  # Start generating permutations from the first position
    return result  # Return the list of permutations


def subsets(nums):
    """Generate all subsets (power set)"""
    result = []  # List to store all subsets

    def backtrack(start, path):
        result.append(path[:])  # Add the current subset to the result

        for i in range(start, len(nums)):  # Iterate through the remaining elements
            path.append(nums[i])  # Include the current element in the subset
            backtrack(
                i + 1, path
            )  # Recurse to generate subsets including the current element
            path.pop()  # Backtrack to exclude the current element

    backtrack(0, [])  # Start generating subsets from the first position
    return result  # Return the list of subsets


# Example usage:
print("\n🔹 Backtracking:")
# Example 1: Permutations
nums9 = [1, 2, 3]
print(f"Permutations of {nums9}: {permute(nums9.copy())}")

# Example 2: Subsets
nums10 = [1, 2, 3]
print(f"Subsets of {nums10}: {subsets(nums10)}")

# Output:
# 🔹 Backtracking:
# Permutations of [1, 2, 3]: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
# Subsets of [1, 2, 3]: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


#####################################
# 🔹 Trie
#####################################


class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to indicate the end of a word


class Trie:
    """Trie implementation for string operations"""

    def __init__(self):
        self.root = TrieNode()  # Initialize the root node

    def insert(self, word):
        node = self.root  # Start from the root node
        for char in word:  # Iterate through each character in the word
            if char not in node.children:  # If the character is not a child, add it
                node.children[char] = TrieNode()
            node = node.children[char]  # Move to the child node
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word):
        node = self.root  # Start from the root node
        for char in word:  # Iterate through each character in the word
            if char not in node.children:  # If the character is not found, return False
                return False
            node = node.children[char]  # Move to the child node
        return node.is_end_of_word  # Return True if the word ends here

    def starts_with(self, prefix):
        node = self.root  # Start from the root node
        for char in prefix:  # Iterate through each character in the prefix
            if char not in node.children:  # If the character is not found, return False
                return False
            node = node.children[char]  # Move to the child node
        return True  # Return True if the prefix exists in the trie


def word_search_ii(board, words):
    """Find all words in a board using a trie"""
    if not board or not board[0] or not words:  # Handle edge cases
        return []

    # Build Trie
    trie = Trie()
    for word in words:  # Insert all words into the trie
        trie.insert(word)

    rows, cols = len(board), len(board[0])  # Get the dimensions of the board
    result = set()  # Use a set to store unique words found

    def dfs(r, c, node, word):
        # Base case: If out of bounds, visited, or character not in trie, return
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or board[r][c] == "#"
            or board[r][c] not in node.children
        ):
            return

        char = board[r][c]  # Get the current character
        node = node.children[char]  # Move to the child node in the trie
        word += char  # Add the character to the current word

        if node.is_end_of_word:  # If the word is complete, add it to the result
            result.add(word)

        board[r][c] = "#"  # Mark the cell as visited

        # Explore all four directions
        dfs(r + 1, c, node, word)
        dfs(r - 1, c, node, word)
        dfs(r, c + 1, node, word)
        dfs(r, c - 1, node, word)

        board[r][c] = char  # Backtrack to restore the cell

    for r in range(rows):  # Iterate through each cell in the board
        for c in range(cols):
            dfs(r, c, trie.root, "")  # Start DFS from each cell

    return list(result)  # Return the list of unique words found


# Example usage:
print("\n🔹 Trie:")
# Example 1: Trie operations
trie = Trie()
words = ["apple", "app", "application", "banana"]
for word in words:
    trie.insert(word)

print(f"Search 'apple' in trie: {trie.search('apple')}")
print(f"Search 'app' in trie: {trie.search('app')}")
print(f"Search 'orange' in trie: {trie.search('orange')}")
print(f"Prefix 'app' in trie: {trie.starts_with('app')}")
print(f"Prefix 'ban' in trie: {trie.starts_with('ban')}")

# Example 2: Word Search II
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
print(f"Word Search II: {word_search_ii(board, words)}")

# Output:
# 🔹 Trie:
# Search 'apple' in trie: True
# Search 'app' in trie: True
# Search 'orange' in trie: False
# Prefix 'app' in trie: True
# Prefix 'ban' in trie: True
# Word Search II: ['oath', 'eat']


#####################################
# 🔹 Bit Manipulation
#####################################


def count_bits(n):
    """Count the number of 1's in the binary representation"""
    count = 0  # Initialize the count of 1's
    while n:  # Continue until all bits are processed
        count += n & 1  # Add 1 if the least significant bit is 1
        n >>= 1  # Right shift the number to process the next bit
    return count  # Return the total count of 1's


def single_number(nums):
    """Find the element that appears only once"""
    result = 0  # Initialize the result with 0
    for num in nums:  # Iterate through all numbers
        result ^= num  # XOR operation cancels out duplicate numbers
    return result  # Return the single number


def power_of_two(n):
    """Check if a number is a power of two"""
    return n > 0 and (n & (n - 1)) == 0  # A power of two has only one bit set


# Example usage:
print("\n🔹 Bit Manipulation:")
# Example 1: Count bits
n = 15
print(f"Count Bits in {n}: {count_bits(n)}")

# Example 2: Single number
nums11 = [4, 1, 2, 1, 2]
print(f"Single Number in {nums11}: {single_number(nums11)}")

# Example 3: Power of two
n = 16
print(f"Is {n} a power of two? {power_of_two(n)}")
n = 15
print(f"Is {n} a power of two? {power_of_two(n)}")

# Output:
# Count Bits in 15: 4
# Single Number in [4, 1, 2, 1, 2]: 4
# Is 16 a power of two? True
# Is 15 a power of two? False


#####################################
# 🔹 Monotonic Stack
#####################################


def next_greater_element(nums):
    """Find the next greater element for each element"""
    result = [-1] * len(nums)  # Initialize the result array with -1
    stack = []  # Stack to store indices of elements

    for i in range(len(nums)):  # Iterate through the array
        # While the stack is not empty and the current element is greater than the element at the index stored in the stack
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]  # Update the result for the popped index
        stack.append(i)  # Push the current index onto the stack

    return result  # Return the array of next greater elements


def largest_rectangle_histogram(heights):
    """Find largest rectangle area in histogram"""
    stack = []  # Stack to store indices of histogram bars
    max_area = 0  # Initialize the maximum area
    i = 0  # Initialize the index

    while i < len(heights):  # Iterate through the histogram
        # If the stack is empty or the current bar is taller than the bar at the top of the stack
        if not stack or heights[stack[-1]] <= heights[i]:
            stack.append(i)  # Push the current index onto the stack
            i += 1  # Move to the next bar
        else:
            top = stack.pop()  # Pop the top index from the stack
            # Calculate the area with the popped bar as the smallest bar
            area = heights[top] * ((i - stack[-1] - 1) if stack else i)
            max_area = max(max_area, area)  # Update the maximum area

    # Process remaining bars in the stack
    while stack:
        top = stack.pop()  # Pop the top index from the stack
        # Calculate the area with the popped bar as the smallest bar
        area = heights[top] * ((i - stack[-1] - 1) if stack else i)
        max_area = max(max_area, area)  # Update the maximum area

    return max_area  # Return the largest rectangle area


# Example usage:
print("\n🔹 Monotonic Stack:")
# Example 1: Next greater element
nums12 = [4, 1, 2, 3]
print(f"Next Greater Element for {nums12}: {next_greater_element(nums12)}")

# Example 2: Largest rectangle in histogram
heights = [2, 1, 5, 6, 2, 3]
print(
    f"Largest Rectangle Area in {heights}: {largest_rectangle_histogram(heights)}"
)

# Output:
# 🔹 Monotonic Stack:
# Next Greater Element for [4, 1, 2, 3]: [-1, 2, 3, -1]
# Largest Rectangle Area in [2, 1, 5, 6, 2, 3]: 10

