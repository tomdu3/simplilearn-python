import datetime
import functools

# define a function that calculates the nth element of the fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memoized(n):
    memo = {}
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n not in memo:
                memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
    return fib(n)

@functools.lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# call functions and check the time it takes
start = datetime.datetime.now()
result_fibonacci = fibonacci(20)
end = datetime.datetime.now()
print('Regular fibonacci took {} seconds'.format(end - start))
print(result_fibonacci)

start = datetime.datetime.now()
result_fibonacci_memoized = fibonacci_memoized(20)
end = datetime.datetime.now()
print(end - start)
print('Memoized fibonacci took {} seconds'.format(end - start))
print(result_fibonacci_memoized)

start = datetime.datetime.now()
result_fibonacci_cached = fibonacci_cached(20)
end = datetime.datetime.now()
print('Cached fibonacci took {} seconds'.format(end - start))
print(result_fibonacci_cached)
