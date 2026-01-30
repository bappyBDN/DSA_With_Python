"""Find geometric sum of the series using recursion
Last Updated : 15 Mar, 2025
Given an integer n, we need to find the geometric sum of the following series using recursion. 

1 + 1/3 + 1/9 + 1/27 + ... + 1/(3n) 

Examples: 

Input: n = 5 
Output: 1.49794
Explanation: 1 + 1/3 + 1/9 + 1/27 + 1/81 + 1/243 = 1.49794

Input: n = 7
Output: 1.49977"""
def sum(n):
    if n == 0:
        return 1
    return (1 / pow(3, n) + sum(n - 1))

n = 5
result = sum(n)
print(result)
