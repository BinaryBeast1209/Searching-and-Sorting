# finding_duplicates.py
# Module: Searching and Sorting - Lesson 1: Linear Search
# Activity 2: FindingDuplicates
# Description: Identifies duplicate elements in a list using linear scanning and frequency tracking.

def find_duplicates_linear(arr):
    """
    Finds duplicate elements using linear checking against a seen list.
    Time Complexity: O(n^2) using lists, or O(n) using sets.
    Space Complexity: O(n)
    """
    seen = []
    duplicates = []
    for item in arr:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.append(item)
    return duplicates


def find_duplicates_freq(arr):
    """
    Finds duplicates by building a frequency map.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return [item for item, count in freq.items() if count > 1]


def main():
    print("=" * 60)
    print("       LESSON 1: LINEAR SEARCH - FINDING DUPLICATES")
    print("=" * 60)

    test_cases = [
        [1, 2, 3, 4, 5, 2, 3, 4, 7, 9, 5],
        [10, 20, 30, 40, 50],
        [4, 4, 4, 4, 4],
        [7, 8, 9, 7, 10, 8, 11]
    ]

    for idx, sample in enumerate(test_cases, 1):
        dups = find_duplicates_linear(sample)
        print(f"Test Case {idx}:")
        print(f"  Array:      {sample}")
        print(f"  Duplicates: {dups if dups else 'None'}")
        print("-" * 55)

    print("\n--- Interactive Test ---")
    user_input = input("Enter numbers separated by spaces (or press Enter for default [5, 2, 8, 2, 9, 5, 1]): ")
    if user_input.strip():
        arr = [int(x) for x in user_input.split()]
    else:
        arr = [5, 2, 8, 2, 9, 5, 1]

    guess = input(f"Guess the duplicate values in {arr}: ")
    result = find_duplicates_linear(arr)
    print(f"Found Duplicates: {result} | Your guess: {guess}")

    print("\n" + "=" * 60)
    print("                     TOPIC SUMMARY")
    print("=" * 60)
    print("1. Linear Scanning compares each incoming item against 'seen' elements.")
    print("2. Frequency counting marks any item with count > 1 as duplicate.")
    print("3. Time Complexity: O(n) with Hash Map / Set; Space Complexity: O(n).")
    print("=" * 60)


if __name__ == "__main__":
    main()
