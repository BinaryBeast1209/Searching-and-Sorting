# max_product.py / acp_max_product.py
# Module: Searching and Sorting - Lesson 6: Sorting Applications
# ACP: MaxProduct
# Description: Finds the maximum product of numbers in an array using sorting (handling positive and negative combinations).

def max_product_pair(nums):
    """
    Finds the maximum product of two distinct elements in an array using sorting.
    Considers both two largest positive numbers and two most negative numbers.
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    if len(nums) < 2:
        return None, ()

    sorted_nums = sorted(nums)
    # Option 1: Two largest numbers
    opt1 = sorted_nums[-1] * sorted_nums[-2]
    # Option 2: Two most negative numbers
    opt2 = sorted_nums[0] * sorted_nums[1]

    if opt1 >= opt2:
        return opt1, (sorted_nums[-2], sorted_nums[-1])
    else:
        return opt2, (sorted_nums[0], sorted_nums[1])


def max_product_triplet(nums):
    """
    Finds the maximum product of three distinct elements in an array.
    Considers:
      Option 1: nums[-1] * nums[-2] * nums[-3] (3 largest)
      Option 2: nums[0] * nums[1] * nums[-1] (2 most negative * 1 largest positive)
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    if len(nums) < 3:
        return None, ()

    sorted_nums = sorted(nums)
    opt1 = sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3]
    opt2 = sorted_nums[0] * sorted_nums[1] * sorted_nums[-1]

    if opt1 >= opt2:
        return opt1, (sorted_nums[-3], sorted_nums[-2], sorted_nums[-1])
    else:
        return opt2, (sorted_nums[0], sorted_nums[1], sorted_nums[-1])


def run_acp_demo():
    print("=" * 65)
    print("       LESSON 6: SORTING APPLICATIONS - ACP: MAX PRODUCT")
    print("=" * 65)
    print("Goal: Find maximum product of pairs and triplets using sorting.\n")

    test_cases = [
        [-10, -10, 5, 2],
        [1, 10, -5, 1, -100],
        [1, 2, 3, 4],
        [-1, -2, -3, -4],
        [3, 4, 5, 2],
        [-4, -3, -2, -1, 60]
    ]

    for idx, arr in enumerate(test_cases, 1):
        pair_val, pair_elems = max_product_pair(arr)
        trip_val, trip_elems = max_product_triplet(arr)

        print(f"Test Case {idx}:")
        print(f"  Array:            {arr}")
        print(f"  Sorted Array:     {sorted(arr)}")
        print(f"  Max Pair Product: {pair_val} (Elements: {pair_elems})")
        if trip_val is not None:
            print(f"  Max Triplet Product: {trip_val} (Elements: {trip_elems})")
        print("-" * 55)

    print("\n--- Interactive Test ---")
    user_input = input("Enter numbers separated by spaces (e.g. -10 -10 5 2) or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            p_val, p_elem = max_product_pair(custom_arr)
            t_val, t_elem = max_product_triplet(custom_arr)
            print(f"\nArray: {custom_arr}")
            print(f"Max Pair Product:    {p_val} from {p_elem}")
            if t_val is not None:
                print(f"Max Triplet Product: {t_val} from {t_elem}")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 65)
    print("                     PROJECT SUMMARY")
    print("=" * 65)
    print("1. Sorting brings extreme values to both ends: smallest (left) and largest (right).")
    print("2. For pairs: max(a[-1]*a[-2], a[0]*a[1]) accounts for negative * negative.")
    print("3. For triplets: max(a[-1]*a[-2]*a[-3], a[0]*a[1]*a[-1]).")
    print("4. Time Complexity: O(n log n) with sorting, Space Complexity: O(1).")
    print("=" * 65)


if __name__ == "__main__":
    run_acp_demo()
