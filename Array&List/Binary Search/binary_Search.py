"""Binary Search is a searching algorithm that operates on a sorted or monotonic search space,
 repeatedly dividing it into halves to find a 
target value or optimal answer in logarithmic time O(log N)."""
def binary_Search(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    target=5
    print(binary_Search(arr,target))
    target1=10
    print(binary_Search(arr,target1))


"""Applications
Searching in sorted arrays
Finding first/last occurrence or closest match in a sorted array
Database indexing — Used in B-trees and similar structures for fast data lookup.
Debugging in version control — Tools like git bisect use binary search to isolate faulty commits.
Network routing & IP lookup — Efficiently find routing entries in tables sorted by address ranges.
File systems & libraries — Fast search through sorted directories or symbol tables.
Gaming/graphics — Collision detection or ray tracing using sorted spatial data.
Machine learning tuning — Efficient hyperparameter search (e.g., learning rate, thresholds).
Optimization problems & competitive programming — Solve boundary-value challenges by narrowing search space.
Advanced data structures — Binary search trees, self-balancing BSTs, and fractional cascading rely on search logic."""