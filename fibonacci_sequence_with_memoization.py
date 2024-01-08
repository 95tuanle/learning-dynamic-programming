def fib(n, cache=None):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    result = fib(n - 1, cache) + fib(n - 2, cache)
    cache[n] = result
    return result
