"""Check if an array is subset of another array
Last Updated : 4 Feb, 2026
Given two arrays a[] and b[] of size m and n respectively, the task is to determine whether b[] is a subset of a[]. Both arrays are not sorted, and elements are distinct.

Examples: 

Input: a[] = [11, 1, 13, 21, 3, 7], b[] = [11, 3, 7, 1] 
Output: true

Input: a[]= [1, 2, 3, 4, 5, 6], b = [1, 2, 4] 
Output: true

Input: a[] = [10, 5, 2, 23, 19], b = [19, 5, 3] 
Output: false"""
#[Naive approach] Using Nested Loops - O(m*n) Time and O(1) Space
def isSubset_naive(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    for i in range(n):
        found=0
        for j in range(m):
            if arr2[i]==arr1[j]:
                found=1
                arr1[j]=-1
                break
        if found==0:
            return False
    return True
#[Better Approach] Using Sorting and Two Pointer - O(m log m + n log n) Time and O(1) space
def isSubset_TwoPointer(arr1,arr2):
    arr1.sort()
    arr2.sort()
    m=len(arr1)
    n=len(arr2)
    i=0
    j=0
    while i<m and j<n:
        if arr1[i]==arr2[j]:
            i+=1
            j+=1
        elif arr2[j]>arr1[i]:
            i+=1
        else:
            return False
    return True
#[Optimal Approach] Using Hashing - O(m+n) Time and O(m) Space
def isSub_set_Hash(arr1,arr2):
    hash_set=set(arr1)
    for num in arr2:
        if num not in hash_set:
            return False
    return True
if __name__ == "__main__":
    arr1=[11, 1, 13, 21, 3, 7]
    arr2=[11, 3, 7, 1]
    #print("Is Subset (Naive):", isSubset_naive(arr1,arr2))
    print("Is Subset (Two Pointer):", isSubset_TwoPointer(arr1,arr2))
    print("Is Subset (Hashing):", isSub_set_Hash(arr1,arr2))
    arr1=[1, 2, 3, 4, 5, 6]
    arr2=[1, 2, 4]
    #print("IS SubSet (Naive):", isSubset_naive(arr1,arr2))

    print("IS SubSet (Two Pointer):", isSubset_TwoPointer(arr1,arr2))
    print("IS SubSet (Hashing):", isSub_set_Hash(arr1,arr2))


    

