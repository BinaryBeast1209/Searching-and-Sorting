# 01_pair_naive.py / pair_of_items_using_naive_approach.py
# Module: Searching and Sorting - Lesson 3: Two Pointers & Pairs
# Activity 1: PairOfItemsUsingNaiveApproach
# Description: Finds a pair of items whose sum equals a target using the O(n^2) nested loop approach.

def find_pair_naive(arr, target):
    """
    Finds a pair of elements (arr[i], arr[j]) with i < j whose sum equals target.
    Uses nested loops to inspect all possible pairs.
    Returns (arr[i], arr[j]) if found, or None.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    comparisons = 0
    for i in range(n):
        for j in range(i + 1, n):
            comparisons += 1
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j]), comparisons
    return None, comparisons


def main():
    print("=" * 65)
    print("   LESSON 3: TWO POINTERS & PAIRS - NAIVE PAIR SEARCH")
    print("=" * 65)
    print("Goal: Check all pairs using nested loops to find sum == target.\n")

    sample_arr = [10, 15, 3, 7, 2, 9, 8]
    test_targets = [17, 10, 19, 99]

    print(f"Sample Array: {sample_arr}\n")

    for target in test_targets:
        pair, steps = find_pair_naive(sample_arr, target)
        if pair:
            print(f"Target {target}: FOUND Pair {pair} ({pair[0]} + {pair[1]} = {target}) in {steps} steps.")
        else:
            print(f"Target {target}: NO pair found (checked all {steps} pairs).")

    print("\n" + "-" * 55)
    print("Interactive Test:")
    user_input = input("Enter numbers separated by spaces (e.g. 2 4 7 11 15) or press Enter for default: ")
    if user_input.strip():
        arr = [int(x) for x in user_input.split()]
    else:
        arr = [2, 4, 7, 11, 15]

    t_input = input("Enter target sum (or press Enter for 18): ")
    target = int(t_input) if t_input.strip() else 18

    pair, steps = find_pair_naive(arr, target)
    if pair:
        print(f"Pair found: {pair} sums to {target} (took {steps} checks).")
    else:
        print(f"No pair found that sums to {target} (checked {steps} pairs).")

    print("\n" + "=" * 65)
    print("                     TOPIC SUMMARY")
    print("=" * 65)
    print("1. Naive approach tests all n*(n-1)/2 pairs using two nested loops.")
    print("2. Outer loop selects first item i; inner loop selects second item j (j > i).")
    print("3. Time Complexity: O(n^2) - becomes slow for large arrays.")
    print("4. Space Complexity: O(1) constant extra space.")
    print("=" * 65)


if __name__ == "__main__":
    main()
