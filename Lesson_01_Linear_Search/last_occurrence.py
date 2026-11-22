# last_occurrence.py / acp_last_occurrence.py
# Module: Searching and Sorting - Lesson 1: Linear Search
# ACP: LastOccurance
# Description: Finds the 0-based index of the LAST occurrence of a target element in a list.

def find_last_occurrence_backward(arr, target):
    """
    Scans from right-to-left (end to beginning).
    Returns the index immediately upon finding the first match from the right.
    Time Complexity: O(n) worst case, O(1) best case if target is at the end.
    Space Complexity: O(1)
    """
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    return -1


def find_last_occurrence_forward(arr, target):
    """
    Scans from left-to-right, continuously updating last_index whenever target matches.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    last_idx = -1
    for i in range(len(arr)):
        if arr[i] == target:
            last_idx = i
    return last_idx


def run_acp_demo():
    print("=" * 60)
    print("      LESSON 1: LINEAR SEARCH - ACP: LAST OCCURRENCE")
    print("=" * 60)
    print("Goal: Find the last index where target element appears.\n")

    test_cases = [
        ([10, 20, 30, 20, 50, 20, 70], 20),
        ([5, 5, 5, 5, 5], 5),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 99),
        ([4, 1, 2, 4, 3, 4, 5], 4)
    ]

    for idx, (arr, target) in enumerate(test_cases, 1):
        last_b = find_last_occurrence_backward(arr, target)
        last_f = find_last_occurrence_forward(arr, target)
        print(f"Test Case {idx}:")
        print(f"  Array: {arr}")
        print(f"  Target: {target}")
        print(f"  Last Occurrence Index: {last_b} ({'Found' if last_b != -1 else 'Not Found'})")
        print(f"  Status: {'PASSED' if last_b == last_f else 'FAILED'}")
        print("-" * 55)

    print("\n--- Interactive Test ---")
    user_input = input("Enter numbers separated by spaces (e.g. 1 3 5 3 7 3 9) or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            t_input = input("Enter target value to find last occurrence of: ")
            target_val = int(t_input)
            ans = find_last_occurrence_backward(custom_arr, target_val)
            print(f"Array: {custom_arr}")
            print(f"Target: {target_val}")
            print(f"Last Occurrence Index: {ans}")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 60)
    print("                     PROJECT SUMMARY")
    print("=" * 60)
    print("1. Standard .index() only returns the FIRST occurrence.")
    print("2. Reverse linear scan (range(len(arr)-1, -1, -1)) is the most efficient method.")
    print("3. Time Complexity: O(n), Space Complexity: O(1).")
    print("=" * 60)


if __name__ == "__main__":
    run_acp_demo()
