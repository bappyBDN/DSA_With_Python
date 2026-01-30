"""Input: 12345
Output: 15
Explanation: Sum of digits → 1 + 2 + 3 + 4 + 5 = 15

Input: 45632
Output: 20 """
def sum_of_digits(n):
    if n==0:
        return 0
    return n%10 + sum_of_digits(n//10)
print(sum_of_digits(12345))
"""Input: 1 2 3 4 5
Output: 3
Explanation: The sum of elements (15) divided by the number of elements (5) gives the mean: 3

Input: 1 2 3
Output: 2
Explanation: The sum of elements (6) divided by the number of elements (3) gives the mean: 2"""
def mean_of_elements(arr, n):
    if n == 0:
        return 0
    return (arr[n-1] + mean_of_elements(arr, n-1))
arr = [1, 2, 3, 4, 5]
n = len(arr)
total_sum = mean_of_elements(arr, n)
mean = total_sum // n
print(mean)
