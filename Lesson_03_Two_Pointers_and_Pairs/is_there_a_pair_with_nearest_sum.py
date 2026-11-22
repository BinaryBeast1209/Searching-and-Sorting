# is_there_a_pair_with_nearest_sum.py / acp_is_there_a_pair_with_nearest_sum.py
# Module: Searching and Sorting - Lesson 3: Two Pointers & Pairs
# ACP: IsThereAPairWithNearestSum
# Description: Checks if an exact pair sum exists, and if not, identifies the pair with the nearest sum.

def check_pair_nearest_sum(arr, target):
    """
    Checks if a pair exists that sums exactly to target.
    If not, finds the pair with the nearest sum to target.
    Uses two-pointer search on sorted array.
    Returns:
      (has_exact_match, closest_pair, closest_sum, difference)
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    if len(arr) < 2:
        return False, None, 0, float("inf")

    sorted_arr = sorted(arr)
    left = 0
    right = len(sorted_arr) - 1

    closest_pair = (sorted_arr[left], sorted_arr[right])
    min_diff = float("inf")
    closest_sum = sorted_arr[left] + sorted_arr[right]
    has_exact = False

    while left < right:
        curr_sum = sorted_arr[left] + sorted_arr[right]
        diff = abs(target - curr_sum)

        if diff < min_diff:
            min_diff = diff
            closest_sum = curr_sum
            closest_pair = (sorted_arr[left], sorted_arr[right])

        if curr_sum == target:
            has_exact = True
            break
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return has_exact, closest_pair, closest_sum, min_diff


def run_acp_demo():
    print("=" * 65)
    print("  LESSON 3: TWO POINTERS - ACP: IS THERE A PAIR WITH NEAREST SUM")
    print("=" * 65)
    print("Goal: Check for exact pair sum; if absent, return nearest pair.\n")

    test_cases = [
        ([10, 22, 28, 29, 30, 40], 54),
        ([1, 4, 45, 6, 10, -8], 16),
        ([10, 20, 30, 40, 50], 72),
        ([2, 3, 5, 8, 9, 11], 17),
        ([5, 12, 19, 21, 35], 40)
    ]

    for idx, (arr, target) in enumerate(test_cases, 1):
        exact, pair, p_sum, diff = check_pair_nearest_sum(arr, target)
        print(f"Test Case {idx}:")
        print(f"  Array:            {arr}")
        print(f"  Target:           {target}")
        print(f"  Exact Pair Exists: {'YES' if exact else 'NO'}")
        print(f"  Nearest Pair:     {pair} (Sum = {p_sum}, Distance from {target} = {diff})")
        print("-" * 55)

    print("\n--- Interactive Test ---")
    user_input = input("Enter numbers separated by spaces (or press Enter to skip): ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            t_input = input("Enter target value to compare against: ")
            target_val = int(t_input)
            exact, pair, p_sum, diff = check_pair_nearest_sum(custom_arr, target_val)
            print(f"\nArray: {custom_arr}")
            print(f"Target: {target_val}")
            print(f"Exact Pair Found: {'YES' if exact else 'NO'}")
            print(f"Nearest Pair: {pair} with Sum = {p_sum} (Difference = {diff})")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 65)
    print("                     PROJECT SUMMARY")
    print("=" * 65)
    print("1. Sort the array first in O(n log n).")
    print("2. Two pointers scan inward in O(n) checking abs(target - sum).")
    print("3. Answers both whether an exact sum pair exists and what the closest pair is.")
    print("4. Total Time Complexity: O(n log n), Auxiliary Space: O(1).")
    print("=" * 65)


if __name__ == "__main__":
    run_acp_demo()
