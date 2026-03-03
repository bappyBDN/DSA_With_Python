"""Find first and last positions of an element in a sorted array
Last Updated : 15 Jan, 2026
Given a sorted array arr[] with possibly some duplicates, the task is to find the first and last occurrences of an element x in the given array.

Note: If the number x is not found in the array then return both the indices as -1.

Examples: 

Input : arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
Output : 2 5
Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5

Input : arr[] = [1, 3, 5, 5, 5, 5, 7, 123, 125 ], x = 7
Output : 6 6
Explanation: First and last occurrence of 7 is at index 6

Input: arr[] = [1, 2, 3], x = 4
Output: -1 -1
Explanation: No occurrence of 4 in the array, so, output is [-1, -1]"""
#[Naive Approach] - Using Iteration - O(n) Time and O(1) Space
def find_1st_last(arr,terget):
    first=-1
    last=-1
    for i in range(len(arr)):
        if(arr[i]==terget):
            if(first==-1):
                first=i
            last=i
    return first,last
#[Efficient Approach] - Using Binary Search - O(log n) Time and O(1) Space
def bin_1st(arr,target):
    low=0
    high=len(arr)-1
    first=-1
    last=-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            first=mid
            
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return first

def bin_last(arr,target):
    low=0
    high=len(arr)-1
    last=-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            last=mid
            
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return last
def find_1st_last_binary(arr,target):


    first=bin_1st(arr,target)
    if first==-1:
        return -1,-1
    last=bin_last(arr,target)
    return first,last

            
            
if __name__ == "__main__":
    arr=[1, 3, 5, 5, 5, 5, 67, 123, 125]
    target=5
    print(find_1st_last(arr,target))
    arr1=[1, 3, 5, 5, 5, 5, 7, 123, 125 ]
    target1=7
    print(find_1st_last(arr1,target1))
    arr2=[1, 2, 3]
    target2=4
    print(find_1st_last(arr2,target2))
    print(find_1st_last_binary(arr,target))
    print(find_1st_last_binary(arr1,target1))
    print(find_1st_last_binary(arr2,target2))
    