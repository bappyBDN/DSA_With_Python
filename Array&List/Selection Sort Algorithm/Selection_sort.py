"""Selection Sort
Last Updated : 8 Dec, 2025
Selection Sort is a comparison-based sorting algorithm. It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.

Find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
Then find the smallest among remaining elements (or second smallest) and swap it with the second element.
We keep doing this until we get all elements moved to correct position."""

def selection_Sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx= j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
def print_arr(arr):
    for i in arr:
        print(i,end=" ")
    print()
if __name__ == "__main__":
    arr=[64, 25, 12, 22, 11]
    print("Before Sorting:")
    print_arr(arr)
    selection_Sort(arr)
    print("\nAfter Sorting:")
    print_arr(arr)