# pair_of_items_using_two_pointers.py
# Module: Searching and Sorting - Lesson 3: Two Pointers & Pairs
# Activity 2: PairOfItemsUsingTwoPointers
# Description: Finds a pair with target sum in a sorted array in O(n) time using inward two pointers.

def find_pair_two_pointers(arr, target):
    """
    Finds a pair (arr[left], arr[right]) in a SORTED array that sums to target.
    Pointers:
      - left starts at index 0 (smallest value)
      - right starts at index n - 1 (largest value)
    Moves inward based on current sum vs target.
    Time Complexity: O(n) (or O(n log n) if sorting is required)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    steps = 0

    while left < right:
        steps += 1
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return (arr[left], arr[right]), steps
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return None, steps


def find_pair_two_pointers_trace(arr, target):
    """Two-pointer search with step-by-step visual trace."""
    print(f"\nSearching for pair summing to {target} in sorted array:\n{arr}")
    left = 0
    right = len(arr) - 1
    step = 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        print(f"  Step {step}: left={left} ({arr[left]}), right={right} ({arr[right]}) -> sum = {curr_sum}")
        if curr_sum == target:
            print(f"    --> TARGET MATCH! Found pair ({arr[left]}, {arr[right]}).")
            return (arr[left], arr[right])
        elif curr_sum < target:
            print(f"    --> Sum {curr_sum} < {target}: Need larger sum, moving left pointer forward (left += 1)")
            left += 1
        else:
            print(f"    --> Sum {curr_sum} > {target}: Need smaller sum, moving right pointer backward (right -= 1)")
            right -= 1
        step += 1

    print("    --> Pointers met. No pair found.")
    return None


def main():
    print("=" * 65)
    print("  LESSON 3: TWO POINTERS & PAIRS - OPTIMAL TWO POINTERS PAIR")
    print("=" * 65)

    sorted_sample = [2, 3, 7, 8, 10, 15, 18, 20]
    find_pair_two_pointers_trace(sorted_sample, 17)
    find_pair_two_pointers_trace(sorted_sample, 25)

    print("\n" + "-" * 55)
    print("Efficiency Comparison: Two Pointers vs Naive Approach:")
    test_arr = list(range(1, 101)) # 100 elements: 1 to 100
    target_val = 199 # 99 + 100

    # Naive count:
    naive_steps = 0
    for i in range(len(test_arr)):
        for j in range(i + 1, len(test_arr)):
            naive_steps += 1
            if test_arr[i] + test_arr[j] == target_val:
                break
        if test_arr[i] + test_arr[j] == target_val:
            break

    pair, tp_steps = find_pair_two_pointers(test_arr, target_val)
    print(f"Array Size: 100 elements. Target: {target_val}")
    print(f"  Two Pointers Steps: {tp_steps} checks   (O(n))")
    print(f"  Naive Approach:     {naive_steps} checks (O(n^2))")
    print(f"  Speedup:            {naive_steps / tp_steps:.1f}x fewer operations!")

    print("\n--- Interactive Test ---")
    user_input = input("\nEnter numbers separated by spaces (or press Enter for default): ")
    if user_input.strip():
        arr = sorted([int(x) for x in user_input.split()])
    else:
        arr = [1, 4, 6, 8, 10, 14, 17, 21]

    t_val = int(input("Enter target sum (or 20): ") or 20)
    res = find_pair_two_pointers_trace(arr, t_val)
    print(f"Result: {res}")

    print("\n" + "=" * 65)
    print("                     TOPIC SUMMARY")
    print("=" * 65)
    print("1. Two pointers inward scan works on SORTED arrays.")
    print("2. If sum < target: left += 1 (increase sum).")
    print("3. If sum > target: right -= 1 (decrease sum).")
    print("4. Reduces complexity from O(n^2) naive to O(n) single pass.")
    print("=" * 65)


if __name__ == "__main__":
    main()
