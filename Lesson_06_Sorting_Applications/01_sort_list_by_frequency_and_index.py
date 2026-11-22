# 01_sort_list_by_frequency_and_index.py / sort_list_by_frequency_and_index.py
# Module: Searching and Sorting - Lesson 6: Sorting Applications
# Activity 1: SortListByFrequency&Index
# Description: Sorts elements of a list by their frequency in descending order,
#              breaking ties by their first appearance index in the original list.

from collections import Counter

def sort_by_frequency_and_index(arr):
    """
    Sorts elements by frequency (highest first).
    Ties in frequency are broken by their original first-occurrence index (earliest first).
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not arr:
        return []

    # Frequency map
    freq = Counter(arr)

    # First occurrence index map
    first_index = {}
    for idx, val in enumerate(arr):
        if val not in first_index:
            first_index[val] = idx

    # Sort key: (-frequency, first_index)
    sorted_arr = sorted(arr, key=lambda x: (-freq[x], first_index[x]))
    return sorted_arr, freq, first_index


def print_detailed_trace(arr):
    print(f"\nOriginal List: {arr}")
    sorted_res, freq_map, idx_map = sort_by_frequency_and_index(arr)
    print("  Element Analysis:")
    unique_elements = list(idx_map.keys())
    for elem in sorted(unique_elements, key=lambda x: (-freq_map[x], idx_map[x])):
        print(f"    Item '{elem}': Frequency = {freq_map[elem]}, First Index = {idx_map[elem]}")
    print(f"  Sorted Result: {sorted_res}")
    return sorted_res


def main():
    print("=" * 65)
    print("  LESSON 6: SORTING APPLICATIONS - SORT BY FREQUENCY & INDEX")
    print("=" * 65)
    print("Primary Sort:   Frequency (Descending - most frequent first)")
    print("Secondary Sort: First Appearance Index (Ascending - tie breaker)\n")

    test_cases = [
        [2, 5, 2, 8, 5, 6, 8, 8],
        [4, 6, 2, 6, 4, 2, 1, 4],
        [10, 20, 10, 30, 40, 20, 50],
        [1, 2, 3, 4, 5],
        [9, 9, 9, 9, 9]
    ]

    for idx, sample in enumerate(test_cases, 1):
        print(f"Test Case {idx}:")
        print_detailed_trace(sample)
        print("-" * 55)

    print("\n--- Interactive Test ---")
    user_input = input("Enter numbers separated by spaces (e.g. 2 5 2 8 5 6 8 8) or press Enter for default: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            print_detailed_trace(custom_arr)
        except ValueError:
            print("Invalid input! Please enter integer values.")
    else:
        print_detailed_trace([3, 1, 4, 4, 5, 2, 6, 1])

    print("\n" + "=" * 65)
    print("                     TOPIC SUMMARY")
    print("=" * 65)
    print("1. Multi-level sorting key: key = lambda x: (-freq[x], first_index[x]).")
    print("2. Negative frequency (-freq[x]) ensures higher counts sort first.")
    print("3. Positive index (first_index[x]) guarantees stable original ordering.")
    print("4. Time Complexity: O(n log n), Space Complexity: O(n).")
    print("=" * 65)


if __name__ == "__main__":
    main()
