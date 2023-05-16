# Problem: 560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array. 

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:
- 1 <= nums.length <= 2 * 104
- -1000 <= nums[i] <= 1000
- -107 <= k <= 107

## Approach:
The given code implements a solution to the subarray sum problem. It uses a prefix sum technique along with a hashmap called 'count' to keep track of the frequencies of prefix sums encountered so far.

For each number 'n' in the given list 'nums', the prefix sum 'prefixSum' is updated by adding 'n'. Then, it checks if there exists a prefix sum 'prefixSum - k' in the hashmap. If it exists, it means there is a subarray with a sum of 'k' ending at the current index. The count of such subarrays is added to the 'answer'.

Finally, the frequency of the current prefix sum is updated in the 'count' hashmap. The 'answer' is returned, representing the total count of subarrays with a sum of 'k'.

## Code: [https://github.com/Ammar-Amjad/Leetcode/blob/main/560.%20Subarray%20Sum%20Equals%20K/code.py](code.py)

## Complexity: time and space complexity
The time complexity of the given solution is O(n), 
where n is the length of the input list 'nums'. This is because the solution iterates through the list once and performs constant time operations for each element.

The space complexity of the solution is O(n).
This is because the 'count' hashmap can potentially store up to n unique prefix sums, where each prefix sum is a key and its frequency is the corresponding value. In the worst case, all elements in the 'nums' list are distinct, resulting in n unique prefix sums. Therefore, the space required by the hashmap is proportional to the length of the input list.