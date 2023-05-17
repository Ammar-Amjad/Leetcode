# Problem: 215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
- 1 <= k <= nums.length <= 105
- -104 <= nums[i] <= 104

## Approach: 

Code: [https://github.com/Ammar-Amjad/Leetcode/tree/main/215.%20Kth%20Largest%20Element%20in%20an%20Arrayy/code.py](code.py)
The provided code uses the QuickSelect algorithm to find the kth largest element in an array. It recursively partitions the array based on a pivot element until it finds the desired element. The function findKthLargest takes the input array and k, then calls the helper function select with appropriate initial arguments. The code efficiently determines the kth largest element by finding the (len(nums) - k)th smallest element in the array.

## Complexity: 
Time complexity : O(N) in the average case, O(N^2) in the worst case.
Space complexity : O(1).      