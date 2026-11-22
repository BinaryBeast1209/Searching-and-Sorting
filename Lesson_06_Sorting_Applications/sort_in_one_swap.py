# sort_in_one_swap.py
# Module: Searching and Sorting - Lesson 6: Sorting Applications
# Activity 2: SortInOneSwap
# Description: Determines if an array can be sorted with at most one swap, and performs the swap in O(n) time.

def sort_in_one_swap(arr):
    """
    Checks if an array can be sorted by swapping at most one pair of elements.
    If possible, returns (True, sorted_array, (i, j)) where i and j are swapped indices.
    If already sorted, returns (True, original_array, None).
    If impossible with one swap, returns (False, original_array, None).
    Time Complexity: O(n)
    Space Complexity: O(1) auxiliary
    """
    a = list(arr)
    n = len(a)
    if n <= 1:
        return True, a, None

    # Step 1: Find inversions from left to right
    first = -1
    second = -1

    for i in range(n - 1):
        if a[i] > a[i + 1]:
            if first == -1:
                first = i
                second = i + 1
            else:
                second = i + 1

    # If no inversion found, array is already sorted
    if first == -1:
        return True, a, None

    # Perform the single swap
    a[first], a[second] = a[second], a[first]

    # Check if array is now completely sorted
    is_sorted = all(a[i] <= a[i + 1] for i in range(n - 1))
    if is_sorted:
        return True, a, (first, second)
    else:
        # Revert back
        a[first], a[second] = a[second], a[first]
        return False, a, None


def main():
    print("=" * 65)
    print("     LESSON 6: SORTING APPLICATIONS - SORT IN ONE SWAP")
    print("=" * 65)
    print("Goal: Check if array can be sorted by swapping at most one pair.\n")

    test_cases = [
        [1, 5, 3, 4, 2],       # False (requires more than 1 swap)
        [1, 2, 5, 4, 3],       # True (swap index 2 and index 4: 5 <-> 3)
        [3, 8, 6, 20, 9],      # False
        [10, 20, 60, 40, 50, 30], # True (swap 60 and 30)
        [1, 2, 3, 4, 5],       # True (already sorted, 0 swaps)
        [2, 1]                 # True (swap 2 and 1)
    ]

    for idx, sample in enumerate(test_cases, 1):
        can_sort, res_arr, indices = sort_in_one_swap(sample)
        print(f"Test Case {idx}:")
        print(f"  Input:            {sample}")
        print(f"  Sortable in 1 Swap: {'YES' if can_sort else 'NO'}")
        if can_sort and indices:
            print(f"  Action Taken:     Swapped index {indices[0]} ({sample[indices[0]]}) <-> index {indices[1]} ({sample[indices[1]]})")
            print(f"  Result Array:     {res_arr}")
        elif can_sort and not indices:
            print("  Action Taken:     Array is already sorted (0 swaps needed).")
        else:
            print("  Action Taken:     Cannot be sorted with a single swap.")
        print("-" * 55)

    print("\n--- Interactive Test ---")
    user_input = input("Enter numbers separated by spaces (e.g. 1 2 5 4 3) or press Enter for default: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
        except ValueError:
            custom_arr = [1, 2, 5, 4, 3]
    else:
        custom_arr = [1, 2, 5, 4, 3]

    can_sort, res_arr, indices = sort_in_one_swap(custom_arr)
    print(f"\nOriginal: {custom_arr}")
    print(f"Can Sort in 1 Swap? {'YES' if can_sort else 'NO'}")
    if can_sort and indices:
        print(f"Swap indices: {indices[0]} <-> {indices[1]} -> Sorted: {res_arr}")
    elif can_sort and not indices:
        print("Already sorted.")
    else:
        print("Requires multiple swaps to sort.")

    print("\n" + "=" * 65)
    print("                     TOPIC SUMMARY")
    print("=" * 65)
    print("1. Identifies first inversion a[i] > a[i+1] and last inversion a[j] > a[j+1].")
    print("2. Swaps a[i] with a[j+1] and verifies if array becomes non-decreasing.")
    print("3. Runs in single pass O(n) time and O(1) space.")
    print("=" * 65)


if __name__ == "__main__":
    main()
