# largest_number.py
# Module: Searching and Sorting - Lesson 5: Selection Sort
# Activity 2: LargestNumber
# Description: Solves both finding the largest element via sorting and forming the largest concatenated number via custom comparator.

from functools import cmp_to_key

def find_largest_element(arr):
    """
    Finds the largest single element in an array using sorting.
    Time Complexity: O(n log n) or O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return None
    sorted_a = sorted(arr)
    return sorted_a[-1]


def form_largest_number(nums):
    """
    Arranges an array of non-negative integers to form the largest combined number.
    Uses Selection Sort with custom comparator:
      For strings a and b, if a + b > b + a, a should come before b.
    Time Complexity: O(n^2)
    Space Complexity: O(n) for string representation
    """
    if not nums:
        return ""

    str_nums = [str(x) for x in nums]
    n = len(str_nums)

    # Selection sort using custom concatenation comparison
    for i in range(n - 1):
        best_idx = i
        for j in range(i + 1, n):
            # Check if putting str_nums[j] before str_nums[best_idx] yields a larger number
            if str_nums[j] + str_nums[best_idx] > str_nums[best_idx] + str_nums[j]:
                best_idx = j

        if best_idx != i:
            str_nums[i], str_nums[best_idx] = str_nums[best_idx], str_nums[i]

    result = "".join(str_nums)
    # Edge case: multiple zeros like [0, 0] should return "0" instead of "00"
    return "0" if result[0] == "0" else result


def main():
    print("=" * 65)
    print("        LESSON 5: SELECTION SORT - LARGEST NUMBER")
    print("=" * 65)
    print("Part 1: Finding maximum element in an array using sorting.")
    print("Part 2: Rearranging elements to form the largest combined number.\n")

    test_cases = [
        [10, 2],
        [3, 30, 34, 5, 9],
        [1, 20, 23, 4, 8],
        [0, 0, 0],
        [54, 546, 548, 60]
    ]

    for idx, nums in enumerate(test_cases, 1):
        largest_elem = find_largest_element(nums)
        combined_largest = form_largest_number(nums)
        print(f"Test Case {idx}:")
        print(f"  Input Numbers:            {nums}")
        print(f"  Largest Single Element:   {largest_elem}")
        print(f"  Largest Formed Number:    '{combined_largest}'")
        print("-" * 55)

    print("\n--- Interactive Test ---")
    user_input = input("Enter non-negative numbers separated by spaces (e.g. 3 30 34 5 9) or press Enter for default: ")
    if user_input.strip():
        try:
            custom_nums = [int(x) for x in user_input.split()]
        except ValueError:
            custom_nums = [3, 30, 34, 5, 9]
    else:
        custom_nums = [3, 30, 34, 5, 9]

    print(f"\nYour Numbers:            {custom_nums}")
    print(f"Largest Single Value:    {find_largest_element(custom_nums)}")
    print(f"Largest Combined Number: '{form_largest_number(custom_nums)}'")

    print("\n" + "=" * 65)
    print("                     TOPIC SUMMARY")
    print("=" * 65)
    print("1. Standard largest element: sorted(arr)[-1] in O(n log n).")
    print("2. Largest concatenated number: compare (a + b) vs (b + a).")
    print("3. Implemented via Selection Sort placing the optimal prefix at each pass.")
    print("4. Handles all-zero edge cases ([0, 0] -> '0').")
    print("=" * 65)


if __name__ == "__main__":
    main()
