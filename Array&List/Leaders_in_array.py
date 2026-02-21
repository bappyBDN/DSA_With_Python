"""Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.

Note: The rightmost element is always a leader.

Examples:

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5 2]
Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader."""
#[Approach 1] Naive approach - O(n^2) Time and O(1) Space
def leaders(arr,n):
    res=[]
    for i in range(0,n):
       
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                
                break
        else:
                res.append(arr[i])
    return res
#[Expected Approach] Using Suffix Maximum - O(n) Time and O(1) Space:
def leaders2(arr,n):
     res=[]
     max_element=arr[n-1]
     res.append(max_element)
     for i in range(n-2,-1,-1):
          if arr[i]>=max_element:
                max_element=arr[i]
                res.append(max_element)
    
     return res[::-1]
if __name__ == "__main__":
    arr=[16, 17, 4, 3, 5, 2]
    n=len(arr)
    print(leaders(arr,n))
    arr1=[1, 2, 3, 4, 5, 2]
    n1=len(arr1)
    print(leaders(arr1,n1)) 
    print(leaders2(arr,n))
    print(leaders2(arr1,n1))
           
   
