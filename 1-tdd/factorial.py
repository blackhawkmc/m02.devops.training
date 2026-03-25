# define your solution
def factorial(n):
    # factorial(n) = n * factorial(n-1)
    if n < 0:
        raise ValueError("Input should be a non-negative integer")
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    result = n * factorial(n-1)
    return result
