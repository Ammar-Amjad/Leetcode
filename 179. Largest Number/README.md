# Problem: 179. Largest Number
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109

## Approach: 
The given approach defines a custom key function, LargerNumKey, which extends the str class. This key function is used to sort a list of integers converted to strings in descending order, based on the concatenation of the numbers. The largestNumber method takes a list of integers, converts them to strings, and sorts them using the LargerNumKey function. The resulting sorted strings are then joined together to form the largest possible number, with a leading '0' if necessary.

## Complexity: 
The time complexity of the largestNumber method is primarily determined by the sorted function. The sorted function has a time complexity of O(n log n), where n is the length of the input list nums. This is because it uses a sorting algorithm (typically Timsort) that has an average case complexity of O(n log n).

The space complexity of the largestNumber method is determined by the space required to store the sorted list of strings. Since the sorted function creates a new sorted list, the space complexity is O(n), where n is the length of the input list nums. Additionally, the space complexity of the largest_num variable, which stores the final largest number as a string, is also O(n), where n is the length of the input list.