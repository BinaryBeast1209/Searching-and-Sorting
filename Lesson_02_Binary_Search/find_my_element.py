# find_my_element.py / acp_find_my_element.py
# Module: Searching and Sorting - Lesson 2: Binary Search
# ACP: FindMyElement
# Description: Comprehensive binary search element finder comparing search steps against linear search.

def binary_search_with_metrics(arr, target):
    """
    Performs binary search while counting the exact number of comparisons made.
    Returns (index, comparisons).
    """
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def linear_search_with_metrics(arr, target):
    """
    Performs linear search while counting comparisons.
    Returns (index, comparisons).
    """
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


def run_acp_demo():
    print("=" * 65)
    print("       LESSON 2: BINARY SEARCH - ACP: FIND MY ELEMENT")
    print("=" * 65)
    print("Goal: Locate target element and demonstrate O(log n) vs O(n) efficiency.\n")

    # Large sorted array of 32 items to clearly show efficiency
    data = [2, 7, 11, 15, 18, 22, 29, 33, 38, 44, 49, 53, 58, 62, 67, 71,
            75, 80, 84, 88, 92, 95, 99, 104, 110, 115, 120, 125, 131, 138, 145, 150]

    test_targets = [88, 2, 150, 67, 100]

    print(f"Dataset Size: {len(data)} sorted elements.")
    print("-" * 65)

    for target in test_targets:
        bs_idx, bs_comp = binary_search_with_metrics(data, target)
        ls_idx, ls_comp = linear_search_with_metrics(data, target)
        found_str = f"Found at index {bs_idx}" if bs_idx != -1 else "Not Present (-1)"
        print(f"Searching for: {target}")
        print(f"  Outcome:                {found_str}")
        print(f"  Binary Search Steps:    {bs_comp} comparisons  (O(log n))")
        print(f"  Linear Search Steps:    {ls_comp} comparisons (O(n))")
        speedup = f"{ls_comp / bs_comp:.1f}x fewer steps" if bs_comp > 0 else "N/A"
        print(f"  Efficiency Advantage:   Binary search was {speedup}!")
        print("-" * 65)

    print("\n--- Try It Yourself ---")
    user_input = input("Enter sorted numbers separated by space (or press Enter to skip): ")
    if user_input.strip():
        try:
            custom_arr = sorted([int(x) for x in user_input.split()])
            t_val = int(input("Enter target number to find: "))
            b_idx, b_steps = binary_search_with_metrics(custom_arr, t_val)
            print(f"Array: {custom_arr}")
            if b_idx != -1:
                print(f"Target {t_val} found at index {b_idx} in {b_steps} steps!")
            else:
                print(f"Target {t_val} not found in array (took {b_steps} steps).")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 65)
    print("                      PROJECT SUMMARY")
    print("=" * 65)
    print("1. For N = 32 elements: Linear search can take up to 32 steps.")
    print("2. Binary search guarantees finding or ruling out in at most log2(32) = 5 steps.")
    print("3. Time Complexity: O(log n), Space Complexity: O(1).")
    print("=" * 65)


if __name__ == "__main__":
    run_acp_demo()
