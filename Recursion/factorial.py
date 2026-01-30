
from matplotlib.pylab import stack


def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)
# Example usage:

#for stack
def factorial_stack(n):
    stack = []
    while n > 0:
        stack.append(n)
        n -=1
    result = 1
    while stack:
        result *= stack.pop()
    return result  

print(factorial_stack(7))  
print(factorial(6))
