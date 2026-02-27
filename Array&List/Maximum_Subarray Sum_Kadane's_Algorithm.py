"""Maximum Subarray Sum - Kadane's Algorithm
Last Updated : 22 Jul, 2025
Given an integer array arr[], find the subarray (containing at least one element) which has the maximum possible sum, and return that sum.
Note: A subarray is a continuous part of an array.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray [-2] has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25."""
#[Naive Approach] By iterating over all subarrays - O(n^2) Time and O(1) Space
def max_subarry_Sum(arr):
    total=arr[0]
    n=len(arr)
    for i in range(n):
        current_sum=0
        for j in range(i,n):
            current_sum += arr[j]
            total = max(total, current_sum)
    return total
#[Optimal Approach] Using Kadane's Algorithm - O(n) Time and O(1) Space
def max_subarry_Sum_Kadens(arr):
    max_sum=arr[0]
    current_sum=arr[0]
    for i in range(1, len(arr)):
        current_sum =max(arr[i], current_sum + arr[i])
        max_sum=max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    arr=[2, 3, -8, 7, -1, 2, 3]
    print(max_subarry_Sum(arr))
    print(max_subarry_Sum_Kadens(arr))
    arr=[-2, -4]
    print(max_subarry_Sum(arr))
    print(max_subarry_Sum_Kadens(arr))
    arr=[5, 4, 1, 7, 8]
    print(max_subarry_Sum(arr))
    print(max_subarry_Sum_Kadens(arr))      
       

