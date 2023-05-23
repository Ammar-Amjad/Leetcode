# Problem: 50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104

## Approach: 
The given code implements a recursive function, myPow, to calculate the result of raising a given number x to the power of n. It uses a divide-and-conquer approach to compute the result efficiently. If n is 0, it returns 1. If n is negative, it converts x to its reciprocal. The recursive function rec recursively calculates the power of x by dividing n by 2 and squaring the result. It then multiplies the intermediate results based on whether n is even or odd. Finally, it returns the computed result.

## Complexity: 
The time complexity of the myPow function in the given code is O(log n), where n is the exponent. This is because the function uses a divide-and-conquer approach, repeatedly dividing the exponent by 2 until it reaches 1, effectively reducing the number of calculations needed. Each division by 2 reduces the exponent by half, resulting in a logarithmic time complexity.

The space complexity of the myPow function is O(log n) as well. This is because the recursive function rec is called recursively for each division by 2. The maximum depth of the recursion is log n, where n is the exponent, as the exponent is halved in each recursive call. Therefore, the space required on the call stack grows logarithmically with respect to the exponent.