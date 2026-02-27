"""
Find the Missing Number
Last Updated : 19 Apr, 2025
Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.

Examples: 

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4
"""
#[Expected Approach 1] Using Sum of n terms Formula - O(n) Time and O(1) Space
def missing_num_Sun(arr):
    n=len(arr)+1
    total_sum=(n*(n+1))//2
    arr_sum=sum(arr)
    return total_sum-arr_sum
#[Expected Approach 2] Using XOR Operator - O(n) Time and O(1) Space

