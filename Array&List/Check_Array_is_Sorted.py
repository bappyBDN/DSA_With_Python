"""Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

Examples: 

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.

Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted."""
#[Approach 1] Iterative approach - O(n) Time and O(1) Space
def is_sorted(arr,n):
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
#[Approach 2] Recursive approach - O(n) Time and O(n) Space
def is_sorted_recursive(arr,n):
    if n==1:
        return True
    if arr[n-2]>arr[n-1]:
        return False
    return is_sorted_recursive(arr,n-1)
#[Approach 3] Using Built-in Methods (Applicable for C++ and Python Only) - O(n) Time and O(1) Space
def is_sorted_STL(arr):
    return arr == sorted(arr)
if __name__ == "__main__":
    arr=[10, 20, 30, 40, 50]
    n=len(arr)
    print(is_sorted(arr,n))
    arr1=[90, 80, 100, 70, 40, 30]
    n1=len(arr1)
    print(is_sorted(arr1,n1))
    print(is_sorted_recursive(arr,n))
    print(is_sorted_recursive(arr1,n1))
    print(is_sorted_STL(arr))
    print(is_sorted_STL(arr1))
