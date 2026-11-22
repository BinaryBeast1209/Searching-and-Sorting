# closest_pair_sum.py
# Module: Searching and Sorting - Lesson 3: Two Pointers & Pairs
# Activity 3: ClosestPairSum
# Description: Finds a pair of elements in an array whose sum is mathematically closest to a target sum.

def closest_pair_sum(arr, target):
    """
    Finds the pair (a, b) in arr whose sum is closest to target.
    Uses sorting followed by the two-pointer technique.
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    if len(arr) < 2:
        return None, 0, 0

    sorted_arr = sorted(arr)
    left = 0
    right = len(sorted_arr) - 1

    closest_pair = (sorted_arr[left], sorted_arr[right])
    min_diff = float("inf")
    best_sum = sorted_arr[left] + sorted_arr[right]

    while left < right:
        curr_sum = sorted_arr[left] + sorted_arr[right]
        diff = abs(target - curr_sum)

        if diff < min_diff:
            min_diff = diff
            best_sum = curr_sum
            closest_pair = (sorted_arr[left], sorted_arr[right])

        if curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
        else:
            # Exact sum match found
            break

    return closest_pair, best_sum, min_diff


def main():
    print("=" * 65)
    print("      LESSON 3: TWO POINTERS & PAIRS - CLOSEST PAIR SUM")
    print("=" * 65)
    print("Goal: Find pair (a, b) whose sum is closest to a given target.\n")

    test_cases = [
        ([10, 22, 28, 29, 30, 40], 54),
        ([1, 3, 4, 7, 10], 15),
        ([-1, 2, 1, -4], 1),
        ([10, 20, 30, 40, 50], 75),
        ([5, 8, 12, 15, 23], 26)
    ]

    for idx, (arr, target) in enumerate(test_cases, 1):
        pair, pair_sum, diff = closest_pair_sum(arr, target)
        print(f"Test Case {idx}:")
        print(f"  Array:        {arr}")
        print(f"  Target:       {target}")
        print(f"  Closest Pair: {pair} -> Sum = {pair_sum} (Difference from {target} = {diff})")
        print("-" * 55)

    print("\n--- Interactive Closest Pair Test ---")
    user_input = input("Enter numbers separated by spaces (e.g. 10 22 28 29 30 40) or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            t_input = input("Enter target sum: ")
            target_val = int(t_input)
            pair, pair_sum, diff = closest_pair_sum(custom_arr, target_val)
            print(f"\nArray: {custom_arr}")
            print(f"Target: {target_val}")
            print(f"Closest Pair Found: {pair}")
            print(f"Pair Sum: {pair_sum} (Distance to target: {diff})")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 65)
    print("                     TOPIC SUMMARY")
    print("=" * 65)
    print("1. Sort array first in O(n log n) time.")
    print("2. Inward two pointers track min_diff = abs(target - (arr[left] + arr[right])).")
    print("3. When sum < target: left += 1; when sum > target: right -= 1.")
    print("4. Early exit when diff == 0 (exact match).")
    print("=" * 65)


if __name__ == "__main__":
    main()
