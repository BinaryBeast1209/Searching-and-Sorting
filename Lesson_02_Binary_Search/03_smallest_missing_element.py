# 03_smallest_missing_element.py / smallest_missing_element.py
# Module: Searching and Sorting - Lesson 2: Binary Search
# Activity 3: SmallestMissingElement
# Description: Finds the smallest missing non-negative integer in a sorted array of distinct integers in O(log n) time.

def find_smallest_missing_binary_search(arr):
    """
    Finds the smallest missing element in a sorted array of distinct non-negative integers.
    Uses modified Binary Search:
      - If arr[mid] == mid: elements 0..mid are all in place, missing is on the RIGHT.
      - If arr[mid] > mid: missing element is on the LEFT (or at mid).
    Returns the value of the smallest missing non-negative integer.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1

    # If first element is not 0, 0 is the smallest missing
    if not arr or arr[0] != 0:
        return 0

    while low <= high:
        mid = (low + high) // 2

        # Check if mid matches its index
        if arr[mid] == mid:
            # Everything before and at mid is complete, search right
            low = mid + 1
        else:
            # arr[mid] > mid, so something is missing on the left
            high = mid - 1

    # At loop termination, 'low' points to the smallest missing integer
    return low


def find_smallest_missing_linear(arr):
    """Linear check for comparison and verification."""
    for i in range(len(arr)):
        if arr[i] != i:
            return i
    return len(arr)


def main():
    print("=" * 60)
    print("   LESSON 2: BINARY SEARCH - SMALLEST MISSING ELEMENT")
    print("=" * 60)
    print("Goal: Find smallest missing non-negative number in sorted array.\n")

    test_cases = [
        [0, 1, 2, 4, 5, 6],
        [1, 2, 3, 4],
        [0, 1, 2, 3, 4, 5],
        [0, 2, 3, 4, 5],
        [0, 1, 3, 6, 8, 9]
    ]

    for idx, arr in enumerate(test_cases, 1):
        bs_ans = find_smallest_missing_binary_search(arr)
        lin_ans = find_smallest_missing_linear(arr)
        print(f"Test Case {idx}:")
        print(f"  Sorted Array:             {arr}")
        print(f"  Smallest Missing (O(log n)): {bs_ans}")
        print(f"  Linear Verification:      {lin_ans}")
        print(f"  Status:                   {'PASSED' if bs_ans == lin_ans else 'FAILED'}")
        print("-" * 55)

    print("\n--- Interactive Test ---")
    user_input = input("Enter sorted distinct non-negative integers (e.g. 0 1 2 3 5 6 7) or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            ans = find_smallest_missing_binary_search(custom_arr)
            print(f"Your Array:               {custom_arr}")
            print(f"Smallest Missing Element: {ans}")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 60)
    print("                     TOPIC SUMMARY")
    print("=" * 60)
    print("1. Key invariant: If no numbers are missing, arr[i] == i for all indices.")
    print("2. The first index where arr[mid] > mid indicates a gap to the left.")
    print("3. Logarithmic time complexity: O(log n) vs O(n) linear scan.")
    print("=" * 60)


if __name__ == "__main__":
    main()
