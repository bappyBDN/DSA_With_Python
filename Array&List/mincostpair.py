"""Minimum cost to make array size 1 by removing larger of pairs
Last Updated : 7 Jul, 2025
Given an array of n integers. We need to reduce size of array to one. We are allowed to select a pair of integers and remove the larger one of these two. This decreases the array size by 1. Cost of this operation is equal to value of smallest one. Find out minimum sum of costs of operations needed to convert the array into a single element.

Examples: 

Input: arr[]= [4 ,3 ,2 ]
Output: 4
Explanation: Choose (4, 2) so 4 is removed, new array = {2, 3}. Now choose (2, 3) so 3 is removed.  So total cost = 2 + 2 = 4.

Input: arr[]=[ 3, 4 ]
Output: 3
Explanation: choose (3, 4) so cost is 3. """
def min_reduction_cost(arr):
    n = len(arr)
    if n <= 1:
        return 0
    
    # 1. Loop to find the minimum element
    min_val = arr[0]
    for i in range(1, n):
        if arr[i] < min_val:
            min_val = arr[i]
            
    # 2. Total cost = min_val * (number of operations)
    total_cost = min_val * (n - 1)
    return total_cost


    
if __name__ == "__main__":
    arr=[4, 3, 2]
    n=len(arr)
    print(min_reduction_cost(arr))
    arr1=[3, 4]
    n1=len(arr1)
    print(min_reduction_cost(arr1))