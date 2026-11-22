# selection_sort_working.py
# Module: Searching and Sorting - Lesson 5: Selection Sort
# Activity 1: SelectionSortWorking
# Description: Demonstrates how Selection Sort works by repeatedly finding the minimum element and placing it at the front.

def selection_sort(arr):
    """
    Standard Selection Sort algorithm.
    Finds the minimum element from the unsorted segment and swaps it into place.
    Returns (sorted_arr, comparisons, swaps).
    Time Complexity: O(n^2) for best, average, and worst cases
    Space Complexity: O(1) in-place
    """
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1

    return a, comparisons, swaps


def selection_sort_visual(arr):
    """
    Selection sort with visual logging of the sorted vs unsorted partitions,
    minimum element selection, and swaps per pass.
    """
    a = list(arr)
    n = len(a)
    print(f"\nInitial Array: {a}")
    print(f"Total elements: {n}\n")
    total_comparisons = 0
    total_swaps = 0

    for i in range(n - 1):
        min_idx = i
        print(f"--- Pass {i + 1} ---")
        print(f"  Sorted part:   {a[:i]}")
        print(f"  Unsorted part: {a[i:]}")
        print(f"  Starting assumption: minimum is a[{i}] = {a[i]}")

        for j in range(i + 1, n):
            total_comparisons += 1
            if a[j] < a[min_idx]:
                print(f"    a[{j}]={a[j]} < a[{min_idx}]={a[min_idx]} -> New minimum found at index {j} (value {a[j]})")
                min_idx = j

        if min_idx != i:
            print(f"  Swap: a[{i}]={a[i]} <-> a[{min_idx}]={a[min_idx]}")
            a[i], a[min_idx] = a[min_idx], a[i]
            total_swaps += 1
        else:
            print(f"  No swap needed: a[{i}]={a[i]} was already the minimum in unsorted part.")

        print(f"  Array after Pass {i + 1}: {a}\n")

    print(f"Sorting Complete! Final Sorted Array: {a}")
    print(f"Total Comparisons: {total_comparisons}, Total Swaps: {total_swaps}")
    return a


def main():
    print("=" * 65)
    print("     LESSON 5: SELECTION SORT - SELECTION SORT WORKING")
    print("=" * 65)
    print("Goal: Understand finding the minimum in unsorted segment & swapping.\n")

    sample = [29, 72, 98, 13, 87]
    selection_sort_visual(sample)

    print("\n" + "-" * 55)
    print("Interactive Selection Sort Trace:")
    user_input = input("Enter numbers separated by spaces (e.g. 64 25 12 22 11) or press Enter for default: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            selection_sort_visual(custom_arr)
        except ValueError:
            print("Invalid input! Please enter integer values.")
    else:
        selection_sort_visual([64, 25, 12, 22, 11])

    print("\n" + "=" * 65)
    print("                     TOPIC SUMMARY")
    print("=" * 65)
    print("1. Divides array into sorted prefix and unsorted suffix.")
    print("2. Scans unsorted part to locate index of smallest element (min_idx).")
    print("3. Swaps min element with first position of unsorted part.")
    print("4. Key advantage over Bubble Sort: at most O(n) swaps (maximum n-1 swaps).")
    print("5. Time Complexity: O(n^2) in all cases, Space Complexity: O(1).")
    print("=" * 65)


if __name__ == "__main__":
    main()
