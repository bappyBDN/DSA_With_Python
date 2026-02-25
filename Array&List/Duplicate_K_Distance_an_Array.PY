"""Duplicate within K Distance in an Array
Last Updated : 23 Jul, 2025
Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. If such a pair exists, return 'Yes', otherwise return 'No'.

Examples: 

Input: k = 3, arr[] = [1, 2, 3, 4, 1, 2, 3, 4]
Output: No
Explanation: Each element in the given array arr[] appears twice and the distance between every element and its duplicate is 4.

Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5]
Output: Yes
Explanation: 1 is present at index 0 and 3.

Input: k = 3, arr[] = [1, 2, 3, 4, 5]
Output: No
Explanation: There is no duplicate element in arr[]."""
#[Naive Approach] - O(n * k) Time and O(1) Space
def DUBLICATE_k_dISTANCE(arr,k):

    l=len(arr)
    for i in range(l):
        for j in range (i+1,l):
            if arr[i]==arr[j ] and abs(i-j)<=k:
                return "Yes"
    return "No"
#[Expected Approach] - Using HashSet - O(n) Time and O(k) Space
def DUBLICATE_k_dISTANCE_set(arr,k):
    s=set()
    for i in range(len(arr)):
        if arr[i] in s:
            return "Yes"
        s.add(arr[i])
        if i>=k:
            s.remove(arr[i-k])
    return "No"

if __name__ == "__main__":
    arr=[1, 2, 3, 4, 1, 2, 3, 4]
    k=3
    print(DUBLICATE_k_dISTANCE(arr,k))
    arr1=[1, 2, 3, 1, 4, 5]
    k1=3
    print(DUBLICATE_k_dISTANCE(arr1,k1))
    arr2=[1, 2, 3, 4, 5]
    k2=3
    print(DUBLICATE_k_dISTANCE(arr2,k2))
    arr3=[1, 2, 3, 4, 1, 2, 3, 4]
    k3=3
    print(DUBLICATE_k_dISTANCE_set(arr3,k3))
    arr4=[1, 2, 3, 1, 4,
    5]
    k4=3
    print(DUBLICATE_k_dISTANCE_set(arr4,k4))

