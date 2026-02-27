"""Given an integer array arr[], compute the sum of all possible sub-arrays of the array. A sub-array is a contiguous part of the array.

Examples: 

Input: arr[] = [1, 4, 5, 3, 2]
Output: 116
Explanation: Sum of all possible subarrays of the array [1, 4, 5, 3, 2] is 116.

Input: arr[] = [1, 2, 3, 4]
Output: 50
Explanation: Sum of all possible subarrays of the array [1, 2, 3, 4] is 50."""
def sum_SUBARRAY(arr):
    l=len(arr)
    
    result=0
    for i in range(l):
        temp=0
        for j in range(i,l):
            temp+=arr[j]
            result+=temp
    return result
#[Expected Approach] Element Contribution Method - O(n) Time and O(1) Space
def sum_Subarray_Combination(arr):
    l=len(arr)
    result=0
    for i in range(l):
        result+=arr[i]*(i+1)*(l-i)
    return result

if __name__=="__main__":
    arr=[1, 4, 5, 3, 2]
    print(sum_SUBARRAY(arr))
    arr1=[1, 2, 3, 4]
    print(sum_SUBARRAY(arr1))
    arr2=[1, 4, 5, 3, 2]
    print(sum_Subarray_Combination(arr2))
    arr3=[1, 2, 3, 4]
    print(sum_Subarray_Combination(arr3))
    
