# define your solution
def fibonacci(n):
    # fibonacci(n-1) + fibonacci(n-2)
    if n < 0:
        raise ValueError("Input should be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)
    return result

