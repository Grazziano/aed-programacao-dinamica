def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(8):
    print()
    if i == 0 or i == 1:
        print(f"Entrada: fibonacci({i}) Para caso base n = {i} retorna {fibonacci(i)}")
    else:
        print(f"Entrada: fibonacci({i}) calcula fibonacci({i-1}) + fibonacci({i-2}) que é {fibonacci(i-1)} + {fibonacci(i-2)}\nSaída: {fibonacci(i)}")
    print()
    print("-"*100)
