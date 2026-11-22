# Searching and Sorting

A comprehensive Python repository implementing foundational search and two-pointer algorithms, created for the Codingal curriculum.

**GitHub Repository:** [https://github.com/BinaryBeast1209/Searching-and-Sorting](https://github.com/BinaryBeast1209/Searching-and-Sorting)

---

## Repository Structure

```
Searching-and-Sorting/
├── Lesson_01_Linear_Search/
│   ├── 01_understanding_linear_search.py
│   ├── understanding_linear_search.py
│   ├── 02_finding_duplicates.py
│   ├── finding_duplicates.py
│   ├── 03_last_occurrence.py
│   ├── last_occurrence.py
│   └── acp_last_occurrence.py
├── Lesson_02_Binary_Search/
│   ├── 01_understanding_binary_search.py
│   ├── understanding_binary_search.py
│   ├── 02_recursive_binary_search.py
│   ├── recursive_binary_search.py
│   ├── 03_smallest_missing_element.py
│   ├── smallest_missing_element.py
│   ├── acp_find_my_element.py
│   └── find_my_element.py
├── Lesson_03_Two_Pointers_and_Pairs/
│   ├── 01_pair_naive.py
│   ├── pair_of_items_using_naive_approach.py
│   ├── 02_pair_two_pointers.py
│   ├── pair_of_items_using_two_pointers.py
│   ├── 03_closest_pair_sum.py
│   └── closest_pair_sum.py
└── README.md
```

---

## Lessons & Activities Breakdown

### Lesson 1: Linear Search (`Lesson_01_Linear_Search/`)

| File / Link | Activity Title | Description | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| `01_understanding_linear_search.py` / `understanding_linear_search.py` | **Activity 1: UnderstandingLinearSearch** | Step-by-step sequential search through elements from index 0 to $n-1$. | $O(n)$ | $O(1)$ |
| `02_finding_duplicates.py` / `finding_duplicates.py` | **Activity 2: FindingDuplicates** | Identifies all duplicate elements via linear scanning and frequency tracking. | $O(n)$ | $O(n)$ |
| `last_occurrence.py` / `acp_last_occurrence.py` | **ACP: LastOccurance** | Reverse linear search from $n-1$ down to 0 to locate the final occurrence index. | $O(n)$ | $O(1)$ |

---

### Lesson 2: Binary Search (`Lesson_02_Binary_Search/`)

| File / Link | Activity Title | Description | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| `01_understanding_binary_search.py` / `understanding_binary_search.py` | **Activity 1: UnderstandingBinarySearch** | Iterative binary search halving the search space each step on a sorted list. | $O(\log n)$ | $O(1)$ |
| `02_recursive_binary_search.py` / `recursive_binary_search.py` | **Activity 2: RecursiveBinarySearch** | Divide-and-conquer binary search using recursive function call stack frames. | $O(\log n)$ | $O(\log n)$ |
| `03_smallest_missing_element.py` / `smallest_missing_element.py` | **Activity 3: SmallestMissingElement** | Modified binary search finding the smallest missing non-negative integer. | $O(\log n)$ | $O(1)$ |
| `find_my_element.py` / `acp_find_my_element.py` | **ACP: FindMyElement** | Element finder demonstrating $O(\log n)$ vs $O(n)$ step efficiency advantages. | $O(\log n)$ | $O(1)$ |

---

### Lesson 3: Two Pointers & Pairs (`Lesson_03_Two_Pointers_and_Pairs/`)

| File / Link | Activity Title | Description | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| `01_pair_naive.py` / `pair_of_items_using_naive_approach.py` | **Activity 1: PairOfItemsUsingNaiveApproach** | Checks all $\frac{n(n-1)}{2}$ pairs using nested loops to find sum matching target. | $O(n^2)$ | $O(1)$ |
| `02_pair_two_pointers.py` / `pair_of_items_using_two_pointers.py` | **Activity 2: PairOfItemsUsingTwoPointers** | Inward two-pointer technique on sorted array to find pair in a single pass. | $O(n)$ | $O(1)$ |
| `03_closest_pair_sum.py` / `closest_pair_sum.py` | **Activity 3: ClosestPairSum** | Finds the pair $(a, b)$ whose sum is mathematically closest to the target. | $O(n \log n)$ | $O(1)$ |

---

## How to Run

### Lesson 1: Linear Search
```bash
python Lesson_01_Linear_Search/01_understanding_linear_search.py
python Lesson_01_Linear_Search/02_finding_duplicates.py
python Lesson_01_Linear_Search/last_occurrence.py
```

### Lesson 2: Binary Search
```bash
python Lesson_02_Binary_Search/01_understanding_binary_search.py
python Lesson_02_Binary_Search/02_recursive_binary_search.py
python Lesson_02_Binary_Search/03_smallest_missing_element.py
python Lesson_02_Binary_Search/find_my_element.py
```

### Lesson 3: Two Pointers & Pairs
```bash
python Lesson_03_Two_Pointers_and_Pairs/01_pair_naive.py
python Lesson_03_Two_Pointers_and_Pairs/02_pair_two_pointers.py
python Lesson_03_Two_Pointers_and_Pairs/03_closest_pair_sum.py
```
