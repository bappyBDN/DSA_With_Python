"""Count 1's in a sorted binary array
Last Updated : 9 Feb, 2026
Given a binary array arr[] of size n, which is sorted in non-increasing order, count the number of 1's in it. 

Examples: 

Input: arr[] = [1, 1, 0, 0, 0, 0, 0]
Output: 2
Explanation: Count of 1's in the given array is 2.

Input: arr[] = [1, 1, 1, 1, 1, 1, 1]
Output: 7

Input: arr[] = [0, 0, 0, 0, 0, 0, 0]
Output: 0"""
#[Naive Approach] - Using Iteration - O(n) Time and O(1) Space
def count_1s(arr):
    cnt=0
    for i in arr:
        if i==1:
            cnt+=1
        else:
            break
    return cnt
#[Efficient Approach] - Using Binary Search - O(log n) Time and O(1) Space
def count_1s_binary(arr):
    n=len(arr)
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==0:

            high=mid-1
        elif  mid<=n-1 and arr[mid+1]!=1:
            return mid+1
        else:
            low=mid+1
    return 0
if __name__ == "__main__":
    arr=[1, 1, 0, 0, 0, 0, 0]
    print(count_1s(arr))
    print(count_1s_binary(arr))
        
