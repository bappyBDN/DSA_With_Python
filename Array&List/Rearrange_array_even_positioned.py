"""Rearrange array such that even positioned are greater than odd
Last Updated : 27 Jan, 2026
Given an array arr[], sort the array according to the following relations:  

arr[i] >= arr[i - 1], if i is even, ∀ 1 <= i < n
arr[i] <= arr[i - 1], if i is odd, ∀ 1 <= i < n
Find the resultant array.[consider 1-based indexing]

Examples:  

Input: arr[] = [1, 2, 2, 1]
Output: [1 2 1 2]
 Explanation:
For i = 2, arr[i] >= arr[i-1]. So, 2 >= 1.
For i = 3, arr[i] <= arr[i-1]. So, 1 <= 2.
For i = 4, arr[i] >= arr[i-1]. So, 2 >= 1.

Input: arr[] = [1, 3, 2]
Output: [1 3 2]
Explanation: 
For i = 2, arr[i] >= arr[i-1]. So, 3 >= 1.
For i = 3, arr[i] <= arr[i-1]. So, 2 <= 3."""

def rearrange(arr):
    l=len(arr)
    for i in range(1,l):
        if ((i+1)%2==0 and arr[i]<arr[i-1]) or ((i+1)%2!=0 and arr[i]>arr[i-1]):
            arr[i],arr[i-1]=arr[i-1],arr[i]
        
    return arr
#[Approach 1] - Assign Maximum Elements to Even Positions
def rearrange_max(arr):
    arr.sort()
    l=len(arr)
    result=[0]*l
    p1=0
    p2=l-1
    for i in range(l):
        if (i+1)%2==0:
            result[i]=arr[p2]
            p2-=1
        else:
            result[i]=arr[p1]
            p1+=1
    return result

if __name__=="__main__":
    arr=[1, 2, 2, 1]
    print(rearrange(arr))
    arr1=[1, 3, 2]
    print(rearrange(arr1))
    arr2=[1, 2, 2, 1]
    print(rearrange_max(arr2))
    arr3=[1, 3, 2]
    print(rearrange_max(arr3))
