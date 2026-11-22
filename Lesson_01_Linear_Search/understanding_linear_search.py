# understanding_linear_search.py
# Module: Searching and Sorting - Lesson 1: Linear Search
# Activity 1: UnderstandingLinearSearch
# Description: Demonstrates the sequential linear search algorithm step by step.

def linear_search(arr, target):
    """
    Performs a linear search on a list for a target value.
    Traverses the list sequentially from index 0 to len(arr)-1.
    Returns the first 0-based index where target is found, or -1 if not found.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_visual(arr, target):
    """
    Performs linear search with step-by-step visual comparison output.
    """
    print(f"\nSearching for target '{target}' in array {arr}...")
    for i, val in enumerate(arr):
        if val == target:
            print(f"  Step {i + 1}: arr[{i}] == {val} -> MATCH FOUND at index {i}!")
            return i
        else:
            print(f"  Step {i + 1}: arr[{i}] == {val} -> Not a match, continuing...")
    print(f"  Reached end of array. Target '{target}' NOT found.")
    return -1


def main():
    print("=" * 60)
    print("    LESSON 1: LINEAR SEARCH - UNDERSTANDING LINEAR SEARCH")
    print("=" * 60)

    # Demo with sample array
    sample = [10, 23, 45, 70, 11, 15]
    print("Sample Array:", sample)
    
    linear_search_visual(sample, 70)
    linear_search_visual(sample, 99)

    print("\n" + "-" * 55)
    print("Interactive Test:")
    user_input = input("Enter numbers separated by spaces (or press Enter for default [12, 45, 23, 89, 34]): ")
    if user_input.strip():
        arr = [int(x) for x in user_input.split()]
    else:
        arr = [12, 45, 23, 89, 34]

    target_input = input("Enter target value to search for (or press Enter for 89): ")
    target = int(target_input) if target_input.strip() else 89

    guess = input(f"What index is {target} at in {arr}? ")
    result = linear_search(arr, target)
    print(f"Result: linear_search({arr}, {target}) = {result} | Your guess: {guess}")

    print("\n" + "=" * 60)
    print("                     TOPIC SUMMARY")
    print("=" * 60)
    print("1. Sequential check: compares arr[i] == target from start to end.")
    print("2. Best Case: O(1) when target is at index 0.")
    print("3. Worst/Average Case: O(n) when target is at the end or absent.")
    print("4. Works on both sorted and unsorted data structures.")
    print("=" * 60)


if __name__ == "__main__":
    main()
