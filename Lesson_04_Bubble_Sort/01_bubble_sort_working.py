# 01_bubble_sort_working.py / bubble_sort_working.py
# Module: Searching and Sorting - Lesson 4: Bubble Sort
# Activity 1: BubbleSortWorking
# Description: Demonstrates how Bubble Sort works step by step with adjacent comparisons and bubbling passes.

def bubble_sort(arr):
    """
    Standard in-place Bubble Sort algorithm.
    Time Complexity: O(n^2) worst/average, O(n) best case (with swapped flag)
    Space Complexity: O(1) in-place
    """
    a = list(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def bubble_sort_visual(arr):
    """
    Bubble sort with detailed pass-by-pass and swap-by-swap visual trace.
    """
    a = list(arr)
    n = len(a)
    print(f"\nInitial Array: {a}")
    total_swaps = 0
    total_comparisons = 0

    for i in range(n):
        print(f"\n--- Pass {i + 1} ---")
        pass_swaps = 0
        swapped = False

        for j in range(0, n - i - 1):
            total_comparisons += 1
            if a[j] > a[j + 1]:
                print(f"  Compare a[{j}]={a[j]} and a[{j+1}]={a[j+1]} -> {a[j]} > {a[j+1]} (SWAP)")
                a[j], a[j + 1] = a[j + 1], a[j]
                pass_swaps += 1
                total_swaps += 1
                swapped = True
                print(f"    Current state: {a}")
            else:
                print(f"  Compare a[{j}]={a[j]} and a[{j+1}]={a[j+1]} -> In order (No swap)")

        print(f"End of Pass {i + 1}: {a} (Swaps in pass: {pass_swaps}, Element '{a[n - i - 1]}' settled)")
        if not swapped:
            print("  --> No swaps occurred in this pass! Array is already fully sorted (Early termination).")
            break

    print(f"\nSorting Complete! Total Comparisons: {total_comparisons}, Total Swaps: {total_swaps}")
    return a


def main():
    print("=" * 65)
    print("       LESSON 4: BUBBLE SORT - BUBBLE SORT WORKING")
    print("=" * 65)
    print("Goal: Understand adjacent comparisons and how values bubble up.\n")

    sample = [5, 1, 4, 2, 8]
    bubble_sort_visual(sample)

    print("\n" + "-" * 55)
    print("Interactive Bubble Sort Trace:")
    user_input = input("Enter numbers separated by spaces (e.g. 64 34 25 12 22 11 90) or press Enter for default: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            bubble_sort_visual(custom_arr)
        except ValueError:
            print("Invalid input! Please enter integer values.")
    else:
        bubble_sort_visual([29, 10, 14, 37, 13])

    print("\n" + "=" * 65)
    print("                     TOPIC SUMMARY")
    print("=" * 65)
    print("1. Repeatedly compares adjacent elements: a[j] and a[j+1].")
    print("2. Swaps if a[j] > a[j+1] so largest values 'bubble' to the right.")
    print("3. After pass i, the last i elements are in their final sorted positions.")
    print("4. Early exit optimization with 'swapped' flag achieves O(n) best case.")
    print("5. Time Complexity: O(n^2), Space Complexity: O(1).")
    print("=" * 65)


if __name__ == "__main__":
    main()
