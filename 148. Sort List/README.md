# Problem: 148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order. 

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: [] 

Constraints:
- The number of nodes in the list is in the range [0, 5 * 104].
- -105 <= Node.val <= 105

## Approach:
The code implements a sorting algorithm for a singly-linked list. It uses a divide-and-conquer approach called merge sort. The main function sortList recursively divides the list into two halves until individual elements are reached. Then it merges the sorted halves back together by calling the merge function.

The sortList function first checks if the list is empty or contains only one element, in which case it returns the list as it is already sorted. Otherwise, it uses the slow and fast pointer technique to find the middle element of the list. It then separates the list into two halves and recursively calls sortList on each half. Finally, it merges the sorted halves using the merge function and returns the sorted list.

The merge function takes two sorted lists as input and merges them into a single sorted list. It creates a dummy node and uses a pointer p to keep track of the current position in the merged list. It iterates through both lists, comparing the values of the nodes, and appends the smaller value to the merged list. After one of the lists is exhausted, it appends the remaining nodes from the other list to the merged list. Finally, it returns the merged list starting from the next node of the dummy node.

Overall, the approach effectively divides the list into smaller subproblems, sorts them individually, and then merges the sorted sublists to obtain the final sorted list.

Code: [https://github.com/Ammar-Amjad/Leetcode/blob/main/148.%20Sort%20List/code.py](code.py)

## Complexity: time and space complexity
The time complexity of the sortList function is O(n log n), 
where n is the number of nodes in the linked list. This is because the function utilizes a merge sort algorithm to sort the linked list recursively. The merge sort algorithm has a time complexity of O(n log n) in the average and worst cases.

The space complexity of the sortList function is O(log n). 
This is because the function uses a recursive approach, and each recursive call adds a new stack frame to the call stack. The maximum depth of the call stack is log n, where n is the number of nodes in the linked list.

The space complexity of the merge function is O(1) 
because it does not use any additional space proportional to the size of the input. It performs the merging in-place by modifying the next pointers of the existing nodes.