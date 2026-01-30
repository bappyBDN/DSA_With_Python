
"""Input: n = 3
Output: 0 1 1

Input: n = 7
Output: 0 1 1 2 3 5 8"""
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
# Example usage:
n=7
for i in range(n):
    print(fibonacci(i), end=" ")