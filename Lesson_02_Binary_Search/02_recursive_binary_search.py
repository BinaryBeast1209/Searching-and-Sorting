# 02_recursive_binary_search.py
# Module: Searching and Sorting - Lesson 2: Binary Search
# Activity 2: RecursiveBinarySearch
# Description: Implements binary search recursively using divide-and-conquer call stacks.

def recursive_binary_search(arr, low, high, target, depth=0):
    """
    Recursively searches for target in sorted array between indices low and high.
    Base cases:
      - low > high: element not found (returns -1)
      - arr[mid] == target: match found (returns mid)
    Recursive step:
      - search left half if arr[mid] > target
      - search right half if arr[mid] < target
    Time Complexity: O(log n)
    Space Complexity: O(log n) call stack frames
    """
    if low > high:
        return -1

    mid = (low + high) // 2
    indent = "  " * depth
    print(f"{indent}[Stack Frame {depth}] Searching range [{low}..{high}], mid={mid} (val={arr[mid]})")

    if arr[mid] == target:
        print(f"{indent}  --> Base Case: Target {target} found at index {mid}!")
        return mid
    elif arr[mid] < target:
        print(f"{indent}  --> {arr[mid]} < {target}: Recursing into right half [{mid + 1}..{high}]")
        return recursive_binary_search(arr, mid + 1, high, target, depth + 1)
    else:
        print(f"{indent}  --> {arr[mid]} > {target}: Recursing into left half [{low}..{mid - 1}]")
        return recursive_binary_search(arr, low, mid - 1, target, depth + 1)


def binary_search_recursive_helper(arr, target):
    """Convenient wrapper taking just array and target."""
    return recursive_binary_search(arr, 0, len(arr) - 1, target)


def main():
    print("=" * 60)
    print("    LESSON 2: BINARY SEARCH - RECURSIVE BINARY SEARCH")
    print("=" * 60)

    sample = [3, 9, 14, 19, 25, 31, 42, 47, 53, 62]
    print("Sorted Array:", sample)

    print("\n--- Trace 1: Target = 42 ---")
    res1 = binary_search_recursive_helper(sample, 42)
    print(f"Result for 42: Index {res1}")

    print("\n--- Trace 2: Target = 15 (Absent) ---")
    res2 = binary_search_recursive_helper(sample, 15)
    print(f"Result for 15: Index {res2}")

    print("\n" + "-" * 55)
    print("Interactive Recursive Binary Search:")
    user_input = input("Enter sorted numbers separated by spaces (or press Enter for default): ")
    if user_input.strip():
        arr = sorted([int(x) for x in user_input.split()])
    else:
        arr = [4, 8, 12, 16, 20, 24, 28, 32]

    t_input = input("Enter target number: ")
    target = int(t_input) if t_input.strip() else 20

    print(f"\nSearching for {target} in {arr}:")
    ans = binary_search_recursive_helper(arr, target)
    print(f"Final Return Value: {ans}")

    print("\n" + "=" * 60)
    print("                     TOPIC SUMMARY")
    print("=" * 60)
    print("1. Recursive formulation reduces problem size by half on each call.")
    print("2. Base case 1: low > high (element not present -> -1).")
    print("3. Base case 2: arr[mid] == target (match found -> mid).")
    print("4. Call stack depth is log2(n), giving O(log n) auxiliary stack space.")
    print("=" * 60)


if __name__ == "__main__":
    main()
