"""
This file contains sample code implementations for common algorithm patterns.
Each pattern includes 2-3 working examples to demonstrate the approach.

https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming

1. Fibonacci Sequence: Utilize when the solution to a problem depends on the solutions of smaller instances of the same problem, resembling the classic Fibonacci sequence.
2. Kadane's Algorithm: Apply to find the maximum sum subarray within a one-dimensional numeric array.
3. 0/1 Knapsack: Use when selecting a subset of items with given weights and values, aiming to maximize total value without exceeding a weight constraint. Each item can be chosen only once.
4. Unbounded Knapsack: Similar to 0/1 Knapsack, but each item can be selected multiple times, allowing for infinite supply of each item.
5. Longest Common Subsequence (LCS): Find a subsequence that appears in the same order in both sequences.
6. Longest Increasing Subsequence (LIS): Determine the longest subsequence where elements are in increasing order.
7. Palindromic Subsequence: Identify the longest subsequence that reads the same forwards and backwards.
8. Edit Distance: Calculate the minimum number of operations required to convert one string into another.
9. Subset Sum: Determine if there's a subset of numbers that adds up to a given sum.
10. String Partition: Divide a string into substrings that satisfy certain conditions.
11. Catalan Numbers: Count the number of ways to correctly match parentheses, among other combinatorial structures.
12. Matrix Chain Multiplication: Determine the most efficient way to multiply a chain of matrices.
13. Count Distinct Ways: Calculate the number of distinct ways to reach a certain point or achieve a goal, often used in pathfinding problems.
14. DP on Grids: Solve problems involving traversing or filling grids, such as finding the number of unique paths.
15. DP on Trees: Apply dynamic programming techniques to tree structures, useful for problems like finding the diameter of a tree.
16. DP on Graphs: Solve problems involving graphs, such as finding the shortest path in weighted graphs.
17. Digit DP: Handle problems involving numbers and their digits, often used in counting problems with constraints.
18. Bitmasking DP: Utilize bitmasks to represent subsets, commonly used in problems involving subsets or combinations.
19. Probability DP: Address problems involving probabilistic outcomes, such as expected values or chances of events occurring.
20. State Machine DP: Model problems using state machines, where the problem's state transitions depend on previous states.
"""

#-----------------------------------------------------------------------------
# Pattern 1: Fibonacci Sequence
#-----------------------------------------------------------------------------
# The Fibonacci pattern is used when a solution depends on solutions to smaller 
# subproblems of the same type. This pattern is the foundation of DP thinking.

# Example 1: Classic Fibonacci with memoization (top-down approach)
def fibonacci_memoization(n, memo={}):
    # Base cases
    if n in memo:  # Check if we've already computed this value
        return memo[n]
    if n <= 1:
        return n
    
    # Calculate and store result for future use
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

# Example 2: Fibonacci with tabulation (bottom-up approach)
def fibonacci_tabulation(n):
    # Edge case
    if n <= 1:
        return n
    
    # Initialize table for storing results
    dp = [0] * (n + 1)
    dp[1] = 1  # Set base cases
    
    # Fill table by computing each subproblem once
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Example usage and expected outputs
print("=== Pattern 1: Fibonacci Sequence ===")
print(f"Fibonacci(10) using memoization: {fibonacci_memoization(10)}")  # Output: 55
print(f"Fibonacci(10) using tabulation: {fibonacci_tabulation(10)}")    # Output: 55

#-----------------------------------------------------------------------------
# Pattern 2: Kadane's Algorithm
#-----------------------------------------------------------------------------
# Kadane's algorithm finds the maximum sum subarray within a one-dimensional array.
# It's elegant in its simplicity and efficiency.

# Example 1: Basic Kadane's algorithm
def kadanes_algorithm(arr):
    if not arr:
        return 0
    
    current_max = global_max = arr[0]
    
    # Iterate through array, maintaining local and global maximums
    for i in range(1, len(arr)):
        # Either extend the previous subarray or start a new one
        current_max = max(arr[i], current_max + arr[i])
        # Update the global maximum if we found a better solution
        global_max = max(global_max, current_max)
    
    return global_max

# Example 2: Kadane with subarray tracking
def kadanes_with_indices(arr):
    if not arr:
        return 0, -1, -1
    
    current_max = global_max = arr[0]
    start = end = global_start = 0
    
    # Track both sum and indices of the maximum subarray
    for i in range(1, len(arr)):
        # Decide to extend previous subarray or start a new one
        if arr[i] > current_max + arr[i]:
            current_max = arr[i]
            start = i  # Mark the start of a new subarray
        else:
            current_max = current_max + arr[i]
        
        # Update global maximum if needed
        if current_max > global_max:
            global_max = current_max
            global_start = start
            end = i
    
    return global_max, global_start, end

# Example usage and expected outputs
print("\n=== Pattern 2: Kadane's Algorithm ===")
print(f"Max subarray sum: {kadanes_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")  # Output: 6
max_sum, start_idx, end_idx = kadanes_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(f"Max subarray sum: {max_sum}, indices: {start_idx} to {end_idx}")  # Output: 6, indices: 3 to 6

#-----------------------------------------------------------------------------
# Pattern 3: 0/1 Knapsack
#-----------------------------------------------------------------------------
# The knapsack pattern applies when selecting from items with different values/weights
# to maximize value while staying within a weight constraint.

# Example 1: Recursive 0/1 Knapsack with memoization
def knapsack_recursive(weights, values, capacity, n, memo={}):
    # Create a unique key for memoization
    key = (n, capacity)
    
    # Base case: no items or no capacity
    if n == 0 or capacity == 0:
        return 0
    
    # Return cached result if available
    if key in memo:
        return memo[key]
    
    # If current item is too heavy, skip it
    if weights[n-1] > capacity:
        memo[key] = knapsack_recursive(weights, values, capacity, n-1, memo)
        return memo[key]
    
    # Find maximum of including or excluding current item
    include = values[n-1] + knapsack_recursive(weights, values, capacity - weights[n-1], n-1, memo)
    exclude = knapsack_recursive(weights, values, capacity, n-1, memo)
    
    memo[key] = max(include, exclude)
    return memo[key]

# Example 2: Iterative 0/1 Knapsack (bottom-up)
def knapsack_tabulation(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP table [items+1][capacity+1]
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the table bottom-up
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If current item can fit
            if weights[i-1] <= w:
                # Max of including or excluding current item
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # If item doesn't fit, we must exclude it
                dp[i][w] = dp[i-1][w]
    
    # Return maximum value achievable
    return dp[n][capacity]

# Example 3: Reconstruct the selected items from Knapsack solution
def knapsack_with_items(weights, values, capacity):
    n = len(weights)
    # Create DP table as in tabulation method
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    
    for i in range(n, 0, -1):
        # If this item was included
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    return dp[n][capacity], selected_items

# Example usage and expected outputs
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

print("\n=== Pattern 3: 0/1 Knapsack ===")
print(f"Max knapsack value (recursive): {knapsack_recursive(weights, values, capacity, len(weights))}")  # Output: 10
print(f"Max knapsack value (tabulation): {knapsack_tabulation(weights, values, capacity)}")             # Output: 10
max_value, items = knapsack_with_items(weights, values, capacity)
print(f"Max value: {max_value}, Selected items (indices): {items}")  # Output: 10, items may vary

#-----------------------------------------------------------------------------
# Pattern 4: Unbounded Knapsack
#-----------------------------------------------------------------------------
# Similar to 0/1 Knapsack, but each item can be selected multiple times.
# Applications: coin change, rod cutting problems.

# Example 1: Unbounded Knapsack with tabulation
def unbounded_knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 1D array to store maximum value at each capacity
    dp = [0] * (capacity + 1)
    
    # Fill the dp table
    for w in range(1, capacity + 1):
        for i in range(n):
            # If current item can fit
            if weights[i] <= w:
                # Maximum of: excluding current item, or including it
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]

# Example 2: Rod cutting problem (special case of unbounded knapsack)
def rod_cutting(prices, rod_length):
    # Create a 1D array to store maximum value for each length
    dp = [0] * (rod_length + 1)
    
    # Fill the dp table bottom-up
    for length in range(1, rod_length + 1):
        max_val = float('-inf')
        # Try all possible cuts
        for cut in range(1, min(length + 1, len(prices) + 1)):
            # prices[cut-1] is the price for a piece of length 'cut'
            max_val = max(max_val, prices[cut-1] + dp[length - cut])
        dp[length] = max_val
    
    return dp[rod_length]

# Example usage and expected outputs
print("\n=== Pattern 4: Unbounded Knapsack ===")
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
print(f"Unbounded Knapsack max value: {unbounded_knapsack(weights, values, capacity)}")  # Output: 12

rod_prices = [1, 5, 8, 9, 10, 17, 17, 20]  # Prices for lengths 1 to 8
print(f"Rod cutting max value: {rod_cutting(rod_prices, 8)}")  # Output: 22

#-----------------------------------------------------------------------------
# Pattern 5: Longest Common Subsequence (LCS)
#-----------------------------------------------------------------------------
# Finds the longest subsequence present in both given sequences.
# A subsequence maintains relative order but doesn't need to be contiguous.

# Example 1: LCS with tabulation
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    # Create a 2D table for storing LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If current characters match
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # Take the maximum of leaving out either character
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Example 2: Reconstruct the LCS
def print_lcs(text1, text2):
    m, n = len(text1), len(text2)
    # Create table as in the previous example
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Backtrack to find the actual LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        # If characters match, include in LCS
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Return LCS in correct order
    return ''.join(reversed(lcs))

# Example usage and expected outputs
print("\n=== Pattern 5: Longest Common Subsequence ===")
str1 = "ABCBDAB"
str2 = "BDCABA"
print(f"Length of LCS: {longest_common_subsequence(str1, str2)}")  # Output: 4
print(f"LCS: {print_lcs(str1, str2)}")  # Output: "BCBA"

#-----------------------------------------------------------------------------
# Pattern 6: Longest Increasing Subsequence (LIS)
#-----------------------------------------------------------------------------
# Finds the longest subsequence where elements are in strictly increasing order.

# Example 1: O(n²) DP approach
def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    
    n = len(nums)
    # dp[i] = length of LIS ending at index i
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            # If current element is greater than previous element
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example 2: O(n log n) approach using patience sort technique
def lis_optimized(nums):
    if not nums:
        return 0
    
    # tails[i] = smallest tail of all increasing subsequences of length i+1
    tails = []
    
    for num in nums:
        # Binary search to find the position to insert num
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If we're at the end, append to tails
        if left == len(tails):
            tails.append(num)
        else:
            # Otherwise replace the tail at position
            tails[left] = num
    
    return len(tails)

# Example usage and expected outputs
print("\n=== Pattern 6: Longest Increasing Subsequence ===")
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Length of LIS (O(n²)): {longest_increasing_subsequence(nums)}")  # Output: 4
print(f"Length of LIS (O(n log n)): {lis_optimized(nums)}")  # Output: 4

#-----------------------------------------------------------------------------
# Pattern 7: Palindromic Subsequence
#-----------------------------------------------------------------------------
# Find the longest subsequence that reads the same forwards and backwards.

# Example 1: Longest Palindromic Subsequence
def longest_palindromic_subsequence(s):
    n = len(s)
    # dp[i][j] = length of LPS in s[i...j]
    dp = [[0] * n for _ in range(n)]
    
    # All single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the table diagonally upwards
    for cl in range(2, n + 1):  # cl is the substring length
        for i in range(n - cl + 1):
            j = i + cl - 1
            # If first and last characters match
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]

# Example 2: Longest Palindromic Substring
def longest_palindromic_substring(s):
    n = len(s)
    # dp[i][j] = true if s[i...j] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    start = 0
    max_length = 1
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # If outer characters match and inner substring is palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length
    
    return s[start:start + max_length]

# Example usage and expected outputs
print("\n=== Pattern 7: Palindromic Subsequence ===")
s = "bbbab"
print(f"Length of longest palindromic subsequence: {longest_palindromic_subsequence(s)}")  # Output: 4
print(f"Longest palindromic substring: {longest_palindromic_substring('babad')}")  # Output: "bab" or "aba"

#-----------------------------------------------------------------------------
# Pattern 8: Edit Distance
#-----------------------------------------------------------------------------
# Calculate minimum operations (insert, delete, replace) to convert one string to another.

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    # dp[i][j] = edit distance between word1[0...i-1] and word2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: empty string to string of length i requires i insertions
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, no operation needed
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Minimum of: insert, delete, replace
                dp[i][j] = 1 + min(
                    dp[i][j-1],    # Insert
                    dp[i-1][j],    # Delete
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]

# Example usage and expected output
print("\n=== Pattern 8: Edit Distance ===")
word1 = "intention"
word2 = "execution"
print(f"Edit distance between '{word1}' and '{word2}': {edit_distance(word1, word2)}")  # Output: 5

#-----------------------------------------------------------------------------
# Pattern 9: Subset Sum
#-----------------------------------------------------------------------------
# Determine if there's a subset that adds up to a given sum.

# Example 1: Basic subset sum (decision problem)
def subset_sum_exists(nums, target_sum):
    n = len(nums)
    # dp[i][j] = True if a subset of nums[0...i-1] sums to j
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    # Empty subset sums to 0
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill the table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If current element is too large, exclude it
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                # dp[i-1][j] = exclude current element
                # dp[i-1][j-nums[i-1]] = include current element
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
    return dp[n][target_sum]

# Example 2: Find all subsets that sum to target
def find_all_subset_sums(nums, target_sum):
    n = len(nums)
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
    # If no subset sums to target
    if not dp[n][target_sum]:
        return []
    
    # Backtrack to find all valid subsets
    def backtrack(i, remaining, current):
        # Base case: found a valid subset
        if remaining == 0:
            result.append(current[:])
            return
        
        # Base case: no more elements or remaining < 0
        if i == 0 or remaining < 0:
            return
        
        # Option 1: Skip current element
        if dp[i-1][remaining]:
            backtrack(i-1, remaining, current)
        
        # Option 2: Include current element if it fits
        if remaining >= nums[i-1] and dp[i-1][remaining - nums[i-1]]:
            current.append(nums[i-1])
            backtrack(i-1, remaining - nums[i-1], current)
            current.pop()
    
    result = []
    backtrack(n, target_sum, [])
    return result

# Example usage and expected outputs
print("\n=== Pattern 9: Subset Sum ===")
nums = [3, 34, 4, 12, 5, 2]
sum1 = 9
sum2 = 10
print(f"Subset sum exists for {sum1}: {subset_sum_exists(nums, sum1)}")  # Output: True
print(f"Subset sum exists for {sum2}: {subset_sum_exists(nums, sum2)}")  # Output: True
print(f"Subsets that sum to {sum1}: {find_all_subset_sums(nums, sum1)}")  # Output: [[4, 5], [3, 4, 2]]

#-----------------------------------------------------------------------------
# Pattern 10: String Partition
#-----------------------------------------------------------------------------
# Partition a string into substrings that satisfy certain conditions.

# Example 1: Palindrome Partitioning
def min_cuts_palindrome_partition(s):
    n = len(s)
    # is_palindrome[i][j] = True if s[i:j+1] is palindrome
    is_palindrome = [[False for _ in range(n)] for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        is_palindrome[i][i] = True
    
    # Check for substrings of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            is_palindrome[i][i+1] = True
    
    # Check for substrings of length 3+
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and is_palindrome[i+1][j-1]:
                is_palindrome[i][j] = True
    
    # dp[i] = minimum cuts needed for s[0:i]
    dp = [float('inf')] * n
    
    for i in range(n):
        # If s[0:i] is palindrome, no cuts needed
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            # Try all possible cuts
            for j in range(i):
                if is_palindrome[j+1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n-1]

# Example usage
print(min_cuts_palindrome_partition("aab"))  # Output: 1 (a|ab)
print(min_cuts_palindrome_partition("ababbbabbababa"))  # Output: 3

# Example 2: Word Break Problem
def word_break(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can be segmented
    
    for i in range(1, n + 1):
        for j in range(i):
            # If we can segment s[0:j] and s[j:i] is in wordDict
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    
    return dp[n]

# Example usage
print("\n=== Pattern 10: String Partition ===")
print(word_break("leetcode", ["leet", "code"]))  # Output: True
print(word_break("applepenapple", ["apple", "pen"]))  # Output: True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False

#-----------------------------------------------------------------------------
# Pattern 11: Catalan Numbers
#-----------------------------------------------------------------------------
# Count the number of ways to correctly match parentheses and other combinatorial structures.

# Example 1: Calculate a single Catalan number using dynamic programming.
def catalan(n):
    # dp[i] will hold the ith Catalan number.
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: C0 = 1
    # Calculate each Catalan number from 1 to n.
    for i in range(1, n+1):
        # Sum over all possible splits.
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    return dp[n]


# Example 2: Generate the first n Catalan numbers.
def catalan_numbers(n):
    # dp[i] stores the ith Catalan number.
    dp = [0] * (n + 1)
    dp[0] = 1  # C0 = 1
    # result list to store the sequence.
    result = [1]
    # Compute Catalan numbers from 1 to n.
    for i in range(1, n+1):
        total = 0
        for j in range(i):
            total += dp[j] * dp[i - j - 1]
        dp[i] = total
        result.append(total)
    return result

# Example usage
print("\n=== Pattern 11: Catalan Numbers ===")
n = 4
# Calculate the 4th Catalan number.
print("Catalan number for {}:".format(n), catalan(n))
# Generate and print the first 6 Catalan numbers.
print("First 6 Catalan numbers:", catalan_numbers(5))

#-----------------------------------------------------------------------------
# Pattern 12: Matrix Chain Multiplication
#-----------------------------------------------------------------------------
# Determine the most efficient way to multiply a chain of matrices.

# Example 1: Calculate the minimum multiplication cost.
def matrix_chain_order(p):
    # p is a list of dimensions such that the ith matrix has dimensions p[i] x p[i+1]
    n = len(p) - 1  # number of matrices
    # dp[i][j] will store the minimum cost of multiplying matrices from i to j.
    dp = [[0] * n for _ in range(n)]
    
    # l is the length of the chain being considered.
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            # Try all possible positions to split the product.
            for k in range(i, j):
                # cost of multiplying the chain from i to k, then k+1 to j, plus cost of final multiplication.
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]


# Example 2: Print the DP table for matrix chain multiplication cost.
def print_matrix_chain_dp(p):
    n = len(p) - 1  # number of matrices
    # Initialize DP table with 0 cost for same matrix multiplication.
    dp = [[0] * n for _ in range(n)]
    
    # Compute cost for multiplying chains of increasing length.
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                dp[i][j] = min(dp[i][j], cost)
    # Print the resulting DP table row by row.
    for row in dp:
        print(row)

# Example usage
print("\n=== Pattern 12: Matrix Chain Multiplication ===")
p = [10, 30, 5, 60]  # Dimensions for three matrices.
print("Minimum multiplication cost:", matrix_chain_order(p))
print("DP table for matrix chain multiplication cost:")
print_matrix_chain_dp(p)

#-----------------------------------------------------------------------------
# Pattern 13: Count Distinct Ways
#-----------------------------------------------------------------------------
# Calculate the number of distinct ways to reach a certain point.

# Example 1: Climbing Stairs (each step can be 1 or 2 steps).
def climb_stairs(n):
    # dp[i] will store the number of ways to reach step i.
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # Base cases: 1 way to stay at 0 and 1 way to reach step 1.
    
    # Compute the ways for each step from 2 to n.
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Sum of ways from the previous two steps.
    return dp[n]


# Example 2: Coin Change (count ways to make change for a given amount).
def coin_change_ways(coins, amount):
    # dp[i] will store the number of ways to form amount i.
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: one way to form amount 0.
    
    # For each coin, update the ways to form amounts from coin value to target amount.
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

# Example usage
print("\n=== Pattern 13: Count Distinct Ways ===")
stairs = 5
# Calculate number of ways to climb 5 stairs.
print("Ways to climb {} stairs:".format(stairs), climb_stairs(stairs))

coins = [1, 2, 5]
amount = 5
# Calculate number of ways to form the amount 5 using coins.
print("Ways to make change for {}:".format(amount), coin_change_ways(coins, amount))

#-----------------------------------------------------------------------------
# Pattern 14: DP on Grids
#-----------------------------------------------------------------------------
# Solve problems involving traversing or filling grids.

# Example 1: Unique Paths in a Grid.
def unique_paths(m, n):
    # Initialize a grid with 1s: only one way to reach cells in the first row or column.
    dp = [[1] * n for _ in range(m)]
    
    # Update the grid for all other cells.
    for i in range(1, m):
        for j in range(1, n):
            # Number of paths to current cell equals sum of paths from top and left cells.
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


# Example 2: Minimum Path Sum in a Grid.
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    # dp[i][j] will store the minimum sum to reach cell (i, j).
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the starting cell.
    dp[0][0] = grid[0][0]
    # Fill the first column.
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    # Fill the first row.
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # Fill in the rest of the grid.
    for i in range(1, m):
        for j in range(1, n):
            # Current cell's value plus the minimum from top or left.
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]

# Example usage
print("\n=== Pattern 14: DP on Grids ===")
m, n = 3, 3
# Calculate the number of unique paths in a 3x3 grid.
print("Unique paths in a {}x{} grid:".format(m, n), unique_paths(m, n))

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
# Calculate the minimum path sum in the grid.
print("Minimum path sum in grid:", min_path_sum(grid))

#-----------------------------------------------------------------------------
# Pattern 15: DP on Trees
#-----------------------------------------------------------------------------
# Apply dynamic programming techniques to tree structures.

# Example 1: Tree Diameter using DP.
class TreeNode:
    def __init__(self, val):
        self.val = val            # Node's value.
        self.children = []        # List to store children of the node.

def tree_diameter(root):
    # Variable to keep track of the largest diameter found.
    diameter = 0

    def dfs(node):
        nonlocal diameter
        if not node:
            return 0
        # max_heights stores the two longest heights among children.
        max_heights = [0, 0]
        # Explore each child.
        for child in node.children:
            h = dfs(child)
            # Update the top two heights.
            if h > max_heights[0]:
                max_heights[1] = max_heights[0]
                max_heights[0] = h
            elif h > max_heights[1]:
                max_heights[1] = h
        # Update the global diameter if the sum of two longest heights is greater.
        diameter = max(diameter, max_heights[0] + max_heights[1])
        # Return the height of the current node.
        return max_heights[0] + 1

    dfs(root)
    return diameter


# Example 2: Maximum Path Sum in a Binary Tree.
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val            # Node's value.
        self.left = None          # Left child.
        self.right = None         # Right child.

def max_path_sum(root):
    # Global variable to keep track of maximum path sum.
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        # Calculate max sum from left and right subtrees (ignore negatives).
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        # Update max_sum considering the current node as root of the path.
        max_sum = max(max_sum, node.val + left + right)
        # Return the max sum path using current node and one subtree.
        return node.val + max(left, right)

    dfs(root)
    return max_sum

# Example usage
print("\n=== Pattern 15: DP on Trees ===")
# Construct a sample tree for diameter.
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)
root.children = [child1, child2]
child1.children = [child3]
# Calculate and print the tree diameter.
print("Tree Diameter:", tree_diameter(root))

# Construct a binary tree for maximum path sum.
broot = BinaryTreeNode(-10)
broot.left = BinaryTreeNode(9)
broot.right = BinaryTreeNode(20)
broot.right.left = BinaryTreeNode(15)
broot.right.right = BinaryTreeNode(7)
# Calculate and print the maximum path sum.
print("Maximum Path Sum in Binary Tree:", max_path_sum(broot))

#-----------------------------------------------------------------------------
# Pattern 16: DP on Graphs
#-----------------------------------------------------------------------------
# Solve problems involving graphs, such as finding the shortest path.

# Example 1: Floyd-Warshall for All-Pairs Shortest Paths.
def floyd_warshall(graph):
    n = len(graph)
    # Create a deep copy of the graph to use as the distance matrix.
    dist = [row[:] for row in graph]
    
    # Iterate through each possible intermediate node.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If going through k is shorter, update the distance.
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


# Example 2: Bellman-Ford for Single Source Shortest Paths.
def bellman_ford(n, edges, source):
    # Initialize distances with infinity.
    dist = [float('inf')] * n
    dist[source] = 0  # Distance from source to itself is 0.
    
    # Relax all edges n-1 times.
    for _ in range(n - 1):
        for u, v, w in edges:
            # If the current path can be improved, update the distance.
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

# Example usage
print("\n=== Pattern 16: DP on Graphs ===")
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]
print("Floyd-Warshall All-Pairs Shortest Paths:")
for row in floyd_warshall(graph):
    print(row)

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (1, 2, 2),
    (2, 3, 7)
]
# Calculate single source shortest paths from node 0.
print("Bellman-Ford Single Source Shortest Paths from 0:", bellman_ford(4, edges, 0))

#-----------------------------------------------------------------------------
# Pattern 17: Digit DP
#-----------------------------------------------------------------------------
# Handle problems involving numbers and their digits with constraints.

# Example 1: Count numbers up to N with a given digit sum.
def count_numbers_with_digit_sum(N, target_sum):
    # Convert the number N into a list of its digits.
    digits = list(map(int, str(N)))
    n = len(digits)
    
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def dp(pos, tight, current_sum):
        # If we've processed all digits, check if the current sum equals target_sum.
        if pos == n:
            return 1 if current_sum == target_sum else 0
        # Set the limit of digits we can place.
        limit = digits[pos] if tight else 9
        count = 0
        # Try every digit from 0 to limit.
        for d in range(limit + 1):
            # Update the 'tight' condition if the chosen digit is exactly the limit.
            count += dp(pos + 1, tight and d == limit, current_sum + d)
        return count

    return dp(0, True, 0)


# Example 2: Count numbers up to N with at most K non-zero digits.
def count_numbers_with_k_nonzero(N, K):
    digits = list(map(int, str(N)))
    n = len(digits)
    
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def dp(pos, tight, count_nonzero):
        # When all digits are processed, check if non-zero count is within K.
        if pos == n:
            return 1 if count_nonzero <= K else 0
        limit = digits[pos] if tight else 9
        total = 0
        # Try every possible digit at current position.
        for d in range(limit + 1):
            # Increase count if digit is non-zero.
            total += dp(pos + 1, tight and d == limit, count_nonzero + (1 if d != 0 else 0))
        return total

    return dp(0, True, 0)

# Example usage
print("\n=== Pattern 17: Digit DP ===")
N = 100
target_sum = 5
# Count numbers less than or equal to 100 with a digit sum of 5.
print("Count numbers <= {} with digit sum {}:".format(N, target_sum), count_numbers_with_digit_sum(N, target_sum))

K = 2
# Count numbers less than or equal to 100 with at most 2 non-zero digits.
print("Count numbers <= {} with at most {} non-zero digits:".format(N, K), count_numbers_with_k_nonzero(N, K))

#-----------------------------------------------------------------------------
# Pattern 18: Bitmasking DP
#-----------------------------------------------------------------------------
# Utilize bitmasks to represent subsets, commonly used in problems like the Traveling Salesman Problem (TSP).

# Example 1: Traveling Salesman Problem (TSP) using Bitmask DP.
def tsp(dist):
    n = len(dist)
    # dp[u][mask]: minimum cost to reach state where 'mask' indicates visited nodes and currently at node u.
    dp = [[float('inf')] * (1 << n) for _ in range(n)]
    dp[0][1] = 0  # Start at node 0 with only node 0 visited.
    
    # Loop over all subsets represented as bit masks.
    for mask in range(1 << n):
        for u in range(n):
            if dp[u][mask] < float('inf'):
                # Try to go to a node v that hasn't been visited.
                for v in range(n):
                    if mask & (1 << v) == 0:
                        new_mask = mask | (1 << v)
                        dp[v][new_mask] = min(dp[v][new_mask], dp[u][mask] + dist[u][v])
    # Return the minimum cost to visit all nodes and return to the starting node.
    return min(dp[u][(1 << n) - 1] + dist[u][0] for u in range(n))


# Example 2: Subset Sum Problem using Bitmask DP (iterative approach).
def subset_sum(nums, target):
    # dp[i] indicates whether a subset sum i is achievable.
    dp = [False] * (target + 1)
    dp[0] = True  # Sum 0 is always achievable.
    # For each number, update the dp table backwards.
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]
    return dp[target]

# Example usage
print("\n=== Pattern 18: Bitmasking DP ===")
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
# Solve the TSP using the provided distance matrix.
print("TSP minimum tour cost:", tsp(dist))

nums = [3, 34, 4, 12, 5, 2]
target = 9
# Check if there is a subset that sums up to the target.
print("Subset sum exists for target {}:".format(target), subset_sum(nums, target))

#-----------------------------------------------------------------------------
# Pattern 19: Probability DP
#-----------------------------------------------------------------------------
# Solve problems involving probabilistic outcomes.

# Example 1: Expected number of coin tosses to get a head (for a biased coin).
def expected_tosses(p):
    # Using the formula: E = 1 / p
    return 1 / p


# Example 2: Expected steps in a simplified board game.
def expected_steps(board, start=0):
    n = len(board)
    # dp[i] stores expected steps from position i.
    dp = [0] * n
    # Process positions in reverse order (from second last to first).
    for i in range(n - 2, -1, -1):
        # Expect one step plus a weighted expected value from next cell.
        dp[i] = 1 + board[i] * dp[i + 1]
    return dp[0]

# Example usage
print("\n=== Pattern 19: Probability DP ===")
p_head = 0.5
# Calculate expected number of tosses for a coin with probability 0.5 of heads.
print("Expected tosses for head with p = {}:".format(p_head), expected_tosses(p_head))

board = [0.5] * 5  # Simplified board: constant probability factor at each step.
# Calculate expected steps on the board starting from index 0.
print("Expected steps on board:", expected_steps(board))

#-----------------------------------------------------------------------------
# Pattern 20: State Machine DP
#-----------------------------------------------------------------------------
# Model problems using state machines, where state transitions depend on previous states.

# Example 1: Count the number of valid strings of length N given state transitions.
def count_valid_strings(N, transitions, start_state, accept_states):
    # dp[(i, state)] represents the count of strings of length i ending in 'state'.
    dp = {}
    dp[(0, start_state)] = 1  # Base case: empty string at start state.
    
    # Process each character position.
    for i in range(N):
        new_dp = {}
        # For each state reached so far, process all transitions.
        for (i_state, state), count in dp.items():
            for char, next_state in transitions.get(state, []):
                # Update count for the next state.
                new_dp[(i + 1, next_state)] = new_dp.get((i + 1, next_state), 0) + count
        dp = new_dp
    # Sum counts for all states that are accepted.
    return sum(count for (i_state, state), count in dp.items() if state in accept_states)


# Example 2: Vending Machine DP simulation.
def vending_machine_dp(N, transitions, start_state, target_state):
    # dp[(i, state)] indicates the count of ways to be in 'state' after i transitions.
    dp = {}
    dp[(0, start_state)] = 1  # Starting state.
    
    # Simulate N transitions.
    for i in range(N):
        new_dp = {}
        for (i_state, state), count in dp.items():
            for money, next_state in transitions.get(state, []):
                new_dp[(i + 1, next_state)] = new_dp.get((i + 1, next_state), 0) + count
        dp = new_dp
    # Return the count of ways to reach the target state after N steps.
    return dp.get((N, target_state), 0)

# Example usage
print("\n=== Pattern 20: State Machine DP ===")
transitions = {
    'A': [('0', 'A'), ('1', 'B')],
    'B': [('0', 'C'), ('1', 'A')],
    'C': [('0', 'B'), ('1', 'C')]
}
N = 5
start_state = 'A'
accept_states = {'A'}
# Count the number of valid strings of length 5 that end in an accept state.
print("Count of valid strings of length {}:".format(N), count_valid_strings(N, transitions, start_state, accept_states))

transitions_vm = {
    'Idle': [(5, 'Ready'), (10, 'Error')],
    'Ready': [(5, 'Idle'), (15, 'Complete')],
    'Error': [(20, 'Idle')],
    'Complete': []
}
# Simulate the vending machine transitions for 3 steps, aiming for 'Complete' state.
print("Vending machine transitions, ways to reach 'Complete' in 3 steps:",
        vending_machine_dp(3, transitions_vm, 'Ready', 'Complete'))