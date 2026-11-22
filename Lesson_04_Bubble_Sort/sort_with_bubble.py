# sort_with_bubble.py / acp_sort_with_bubble.py
# Module: Searching and Sorting - Lesson 4: Bubble Sort
# ACP: SortWithBubble
# Description: After-Class Project demonstrating Bubble Sort with customizable sort orders, metrics, and real-world datasets.

def sort_with_bubble(arr, ascending=True):
    """
    Sorts a list using the Bubble Sort algorithm.
    Parameters:
      arr: list to sort
      ascending: True for ascending order, False for descending order
    Returns:
      (sorted_list, comparisons, swaps, passes)
    Time Complexity: O(n^2) worst/average, O(n) best
    Space Complexity: O(1) in-place
    """
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n):
        passes += 1
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            should_swap = (a[j] > a[j + 1]) if ascending else (a[j] < a[j + 1])
            if should_swap:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return a, comparisons, swaps, passes


def run_acp_demo():
    print("=" * 65)
    print("        LESSON 4: BUBBLE SORT - ACP: SORT WITH BUBBLE")
    print("=" * 65)
    print("Goal: Sort datasets in ascending and descending order using Bubble Sort.\n")

    datasets = [
        ("Student Exam Scores", [85, 92, 78, 64, 99, 88, 73]),
        ("Daily Temperatures",  [32, 28, 35, 30, 27, 31, 29]),
        ("Sports Team Ranks",   [64, 34, 25, 12, 22, 11, 90]),
        ("Already Sorted Data", [10, 20, 30, 40, 50, 60, 70])
    ]

    for title, data in datasets:
        asc_sorted, asc_c, asc_s, asc_p = sort_with_bubble(data, ascending=True)
        desc_sorted, desc_c, desc_s, desc_p = sort_with_bubble(data, ascending=False)

        print(f"Dataset: {title}")
        print(f"  Original:   {data}")
        print(f"  Ascending:  {asc_sorted} (Comparisons: {asc_c}, Swaps: {asc_s}, Passes: {asc_p})")
        print(f"  Descending: {desc_sorted} (Comparisons: {desc_c}, Swaps: {desc_s}, Passes: {desc_p})")
        print("-" * 65)

    print("\n--- Interactive Bubble Sort ---")
    user_input = input("Enter numbers separated by spaces (or press Enter to skip): ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            order_choice = input("Sort order - (A)scending or (D)escending? [Default A]: ").strip().upper()
            is_asc = order_choice != "D"
            result, c, s, p = sort_with_bubble(custom_arr, ascending=is_asc)
            direction_str = "Ascending" if is_asc else "Descending"
            print(f"\nOriginal:   {custom_arr}")
            print(f"Sorted ({direction_str}): {result}")
            print(f"Execution Stats: {c} comparisons, {s} swaps, completed in {p} pass(es).")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 65)
    print("                     PROJECT SUMMARY")
    print("=" * 65)
    print("1. Compares adjacent elements and swaps them into correct order.")
    print("2. Largest (or smallest) elements float to their final positions each pass.")
    print("3. Early break flag prevents unnecessary passes when list is sorted.")
    print("4. Time Complexity: O(n^2) worst/average, O(n) best-case.")
    print("5. Space Complexity: O(1) in-place auxiliary space.")
    print("=" * 65)


if __name__ == "__main__":
    run_acp_demo()
