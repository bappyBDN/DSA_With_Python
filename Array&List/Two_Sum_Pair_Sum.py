"""Two Sum - Pair with given Sum
Last Updated : 26 Jul, 2025
Given an array arr[] of n integers and a target value, check if there exists a pair whose sum equals the target. This is a variation of the 2-Sum problem.

Examples: 

Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: true
Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.

Input: arr[] = [1, -2, 1, 0, 5], target = 0
Output: false
Explanation: There is no pair with sum equals to given target."""
#[Naive Approach] By iterating over all pairs - O(n^2) Time and O(1) Space
def Two_Sum_Pair_Sum(arr, target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return True
    return False
#[Better Approach 2] Sorting and Two-Pointer Technique - O(n × log(n)) time and O(1) space
def Two_Pointer_Sort(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<right:
        current_sum=arr[left]+arr[right]
        if current_sum==target:
            return True
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return False

#[Optimal Approach] Using Hashing - O(n) Time and O(n) Space
def Two_Sum_Hash(arr, target):
    s=set()
    for n in arr:
        if target-n in s:
            return True
        s.add(n)
    return False
if __name__ == "__main__":
    arr=[0, -1, 2, -3, 1]
    target=-2
    print(Two_Sum_Pair_Sum(arr,target))
    print(Two_Pointer_Sort(arr,target))
    print(Two_Sum_Hash(arr,target))
    arr=[1, -2, 1, 0, 5]
    target=0
    print(Two_Sum_Pair_Sum(arr,target))
    print(Two_Pointer_Sort(arr,target))
    print(Two_Sum_Hash(arr,target))
