"""Unique Number I
Last Updated : 23 Jul, 2025
Given an array of integers, every element in the array appears twice except for one element which appears only once. The task is to identify and return the element that occurs only once.

Examples: 

Input:  arr[] = [2, 3, 5, 4, 5, 3, 4]
Output: 2 
Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.

Input: arr[] = [2, 2, 5, 5, 20, 30, 30]
Output: 20
Explanation: Since 20 occurs once, while other numbers occur twice, 20 is the answer."""
#[Naive Approach] - O(n^2) Time and O(1) Space
def unique_number(arr):
    l=len(arr)
    for i in range(l):
        count=0
        for j in range(l):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            return arr[i]
#[Expected Approach] - Using XOR Operator - O(n) Time and O(1) Space
def unique_number_xor(arr):
    res=0
    for i in range(len(arr)):
        res^=arr[i]
    return res
#[Better Approach] Using Hash Map - O(n) Time and O(n) Space
def unique_number_hash(arr):
    d={}
    for i in range(len(arr)):
        d[arr[i]]=d.get(arr[i],0)+1
    for key in d:
        if d[key]==1:
            return key
    return -1

if __name__=="__main__":
    arr=[2, 3, 5, 4, 5, 3, 4]
    print(unique_number(arr))
    arr1=[2, 2, 5, 5, 20, 30, 30]
    print(unique_number(arr1))
    arr2=[2, 3, 5, 4, 5, 3, 4]
    print(unique_number_xor(arr2))
    arr3=[2, 2, 5, 5, 20, 30, 30]
    print(unique_number_xor(arr3))
    arr4=[2, 3, 5, 4, 5, 3, 4]
    print(unique_number_hash(arr4))
