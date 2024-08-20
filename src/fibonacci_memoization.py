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

for i in range(8):
    print()
    if i == 0 or i == 1:
        print(f"Para caso base para n = {i} retorna {i}")
    else:
        print(f"Entrada: fibonacci_memo({i}) calcula fibonacci_memo({i-1}) + fibonacci_memo({i-2}) que é {fibonacci_memo(i-1, memo={})} + {fibonacci_memo(i-2, memo={})}\nSaída: {fibonacci_memo(i, memo={})}")
    print()
    print("-"*100)
