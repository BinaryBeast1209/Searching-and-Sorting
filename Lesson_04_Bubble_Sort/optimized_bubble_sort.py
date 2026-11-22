# optimized_bubble_sort.py
# Module: Searching and Sorting - Lesson 4: Bubble Sort
# Activity 2: OptimizedBubbleSort
# Description: Implements Bubble Sort with the swapped flag optimization to achieve O(n) best-case time complexity.

def optimized_bubble_sort(arr):
    """
    Optimized Bubble Sort using swapped flag.
    Exits early if an entire pass completes without any swaps.
    Returns (sorted_arr, comparisons, passes_taken).
    Time Complexity: O(n) Best Case, O(n^2) Worst/Average Case
    Space Complexity: O(1) in-place
    """
    a = list(arr)
    n = len(a)
    comparisons = 0
    passes_taken = 0

    for i in range(n):
        passes_taken += 1
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        # If no two elements were swapped in this pass, array is sorted!
        if not swapped:
            break

    return a, comparisons, passes_taken


def unoptimized_bubble_sort(arr):
    """
    Standard unoptimized Bubble Sort for comparison.
    Always runs through all n*(n-1)//2 comparisons regardless of order.
    """
    a = list(arr)
    n = len(a)
    comparisons = 0
    passes_taken = 0

    for i in range(n):
        passes_taken += 1
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a, comparisons, passes_taken


def main():
    print("=" * 65)
    print("      LESSON 4: BUBBLE SORT - OPTIMIZED BUBBLE SORT")
    print("=" * 65)
    print("Goal: Use the 'swapped' boolean flag to break early when array is sorted.\n")

    # Benchmark test cases
    benchmarks = [
        ("Already Sorted Array", [1, 2, 3, 4, 5, 6, 7, 8]),
        ("Nearly Sorted Array",  [1, 2, 3, 5, 4, 6, 7, 8]),
        ("Reverse Sorted Array", [8, 7, 6, 5, 4, 3, 2, 1]),
        ("Random Unsorted Array",[64, 34, 25, 12, 22, 11, 90])
    ]

    for title, data in benchmarks:
        opt_sorted, opt_comp, opt_passes = optimized_bubble_sort(data)
        unopt_sorted, unopt_comp, unopt_passes = unoptimized_bubble_sort(data)

        print(f"Benchmark: {title}")
        print(f"  Input:                   {data}")
        print(f"  Optimized Bubble Sort:   {opt_comp} comparisons in {opt_passes} pass(es)  (O(n) best-case)")
        print(f"  Standard Bubble Sort:    {unopt_comp} comparisons in {unopt_passes} passes (O(n^2))")
        if unopt_comp > opt_comp:
            print(f"  --> Optimization Saved:  {unopt_comp - opt_comp} redundant comparisons!")
        else:
            print("  --> (Worst case: full passes required for reversed array)")
        print("-" * 65)

    print("\n--- Interactive Optimized Bubble Sort ---")
    user_input = input("Enter numbers separated by spaces (or press Enter for default): ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
        except ValueError:
            custom_arr = [10, 20, 30, 25, 50, 60]
    else:
        custom_arr = [10, 20, 30, 25, 50, 60]

    s_arr, comps, passes = optimized_bubble_sort(custom_arr)
    print(f"\nOriginal: {custom_arr}")
    print(f"Sorted:   {s_arr}")
    print(f"Stats:    Sorted in {comps} comparisons across {passes} pass(es).")

    print("\n" + "=" * 65)
    print("                     TOPIC SUMMARY")
    print("=" * 65)
    print("1. Standard Bubble Sort always does n*(n-1)/2 comparisons.")
    print("2. Optimized version tracks 'swapped' flag during each pass.")
    print("3. If swapped == False: Array is confirmed sorted, break immediately.")
    print("4. Best-Case Time Complexity: O(n) (single pass of n-1 comparisons).")
    print("5. Worst/Average Time Complexity: O(n^2), Space Complexity: O(1).")
    print("=" * 65)


if __name__ == "__main__":
    main()
