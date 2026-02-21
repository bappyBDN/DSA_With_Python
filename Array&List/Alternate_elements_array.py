"""Given an array arr[], the task is to print every alternate element of the array starting from the first element.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12"""
def alternete_element(arr):
    res=[]
    for i in range(0,len(arr),2):
        res.append(arr[i])
    return res
#Recursive approach
def alternate_element_recursive(arr,index=0):
    res=[]
    if index>=len(arr):
        return res
    res.append(arr[index])
    res.extend(alternate_element_recursive(arr,index+2))
    return res
    
if __name__ == "__main__":
    arr=[10, 20, 30, 40, 50]
    print(alternete_element(arr))
    arr1=[-5, 1, 4, 2, 12]
    print(alternete_element(arr1))
    print(alternate_element_recursive(arr))
    print(alternate_element_recursive(arr1))

