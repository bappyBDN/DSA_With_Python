"""Max Distance Between Two Occurrences
Last Updated : 23 Jul, 2025
Given an array arr[], the task is to find the maximum distance between two occurrences of any element. If no element occurs twice, return 0.

Examples:  

Input: arr = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is: 4-2 = 2, So max distance is 5.

Input : arr[] = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation : Max distance for 2 is 11-1 = 10, max distance for 1 is 4-2 = 2 and max distance for 4 is 10-5 = 5  

Input: arr[] = [1, 2, 3, 6, 5, 4]
Output: 0
Explanation: No element has two occurrence, so maximum distance = 0."""
#[Brute Force Approach] - O(n^2) Time and O(1) Space
def max_distance(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if arr[i]==arr[j]:
                return j-i
    return 0
#[Optimal Approach] Using Hashing - O(n) Time and O(n) Space
def max_distance_hash(arr):
    hash_map={}
    max_distance=0
    for i in range(len(arr)):
        if arr[i] in hash_map:
            max_distance=max(max_distance,i-hash_map[arr[i]])
        else:
            hash_map[arr[i]]=i
    return max_distance
if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 1]
    print("Max Distance:", max_distance(arr))
    print("Max Distance (Hashing):", max_distance_hash(arr))
    arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
    print("Max Distance:", max_distance(arr))
    print("Max Distance (Hashing):", max_distance_hash(arr))
    arr = [1, 2, 3, 6, 5, 4]
    print("Max Distance:", max_distance(arr))
    print("Max Distance (Hashing):", max_distance_hash(arr))