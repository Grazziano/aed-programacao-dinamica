def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = result
        return result
