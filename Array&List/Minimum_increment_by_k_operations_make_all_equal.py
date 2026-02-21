"""You are given an array of n-elements, you have to find the number of operations needed to make all elements of array equal. Where a single operation can increment an element by k. If it is not possible to make all elements equal print -1.

Example : 

Input : arr[] = {4, 7, 19, 16},  k = 3
Output : 10

Input : arr[] = {4, 4, 4, 4}, k = 3
Output : 0

Input : arr[] = {4, 2, 6, 8}, k = 3
Output : -1

To solve this question we require to check whether all elements can became equal or not and that too only by incrementing k from elements value. For this we have to check that the difference of any two elements should always be divisible by k. If it is so, then all elements can become equal otherwise they can not became equal in any case by incrementing k from them. Also, the number of operations required can be calculated by finding value of (max - Ai)/k for all elements. where max is maximum element of array.

Algorithm : 

// iterate for all elements
for (int i=0; i<n; i++)
{
    // check if element can make equal to max
    //  or not if not then return -1
    if ((max - arr[i]) % k != 0 )
        return -1;

    // else update res for required operations
    else
        res += (max - arr[i]) / k ;
}

return res;"""
def min_Oprs(arr,n,k):
    max_element=max(arr)
    res=0
    for i in range(0,n):
        if (max_element-arr[i])%k!=0:
            return -1
        else:
            res+=((max_element-arr[i])/k)
    return res
if __name__ == "__main__":
    arr=[4, 7, 19, 16]
    n=len(arr)
    k=3
    print(min_Oprs(arr,n,k))
    arr1=[4, 4, 4, 4]
    n1=len(arr1)
    k1=3
    print(min_Oprs(arr1,n1,k1))
    arr2=[4, 2, 6, 8]
    n2=len(arr2)
    k2=3
    print(min_Oprs(arr2,n2,k2))
    arr5 = [21, 33, 9, 45, 63] 
    n = len(arr5)
    k = 6
    print(min_Oprs(arr5, n, k))