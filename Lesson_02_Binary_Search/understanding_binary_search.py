# understanding_binary_search.py
# Module: Searching and Sorting - Lesson 2: Binary Search
# Activity 1: UnderstandingBinarySearch
# Description: Demonstrates iterative binary search on a sorted list by halving search space.

def binary_search(arr, target):
    """
    Standard iterative binary search on sorted array.
    Returns 0-based index of target if found, else -1.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_trace(arr, target):
    """
    Binary search with step-by-step visual logging of low, mid, high, and arr[mid].
    """
    print(f"\nTracing Binary Search for target '{target}' in sorted array:\n{arr}")
    low = 0
    high = len(arr) - 1
    step = 1

    while low <= high:
        mid = (low + high) // 2
        print(f"  Step {step}: low={low}, high={high}, mid={mid} -> arr[{mid}] = {arr[mid]}")
        
        if arr[mid] == target:
            print(f"    --> MATCH! Target '{target}' found at index {mid}.")
            return mid
        elif arr[mid] < target:
            print(f"    --> {arr[mid]} < {target}. Target is in RIGHT half. Updating low = {mid + 1}")
            low = mid + 1
        else:
            print(f"    --> {arr[mid]} > {target}. Target is in LEFT half. Updating high = {mid - 1}")
            high = mid - 1
        step += 1

    print(f"    --> low > high. Target '{target}' is NOT in array.")
    return -1


def main():
    print("=" * 60)
    print("   LESSON 2: BINARY SEARCH - UNDERSTANDING BINARY SEARCH")
    print("=" * 60)

    sample = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    binary_search_trace(sample, 23)
    binary_search_trace(sample, 40)

    print("\n" + "-" * 55)
    print("Interactive Binary Search Test:")
    user_input = input("Enter sorted numbers separated by spaces (or press Enter for default [10, 20, 30, 40, 50, 60, 70]): ")
    if user_input.strip():
        arr = sorted([int(x) for x in user_input.split()])
    else:
        arr = [10, 20, 30, 40, 50, 60, 70]

    t_input = input("Enter target value (or press Enter for 50): ")
    target = int(t_input) if t_input.strip() else 50

    guess = input(f"Guess the index of {target} in {arr}: ")
    ans = binary_search(arr, target)
    print(f"Result: binary_search({arr}, {target}) = {ans} | Your guess: {guess}")

    print("\n" + "=" * 60)
    print("                     TOPIC SUMMARY")
    print("=" * 60)
    print("1. Binary search requires the dataset to be SORTED.")
    print("2. Halves search interval at each step: O(log n) time complexity.")
    print("3. Best Case: O(1) if target is at mid on step 1.")
    print("4. Worst/Average Case: O(log n).")
    print("=" * 60)


if __name__ == "__main__":
    main()
