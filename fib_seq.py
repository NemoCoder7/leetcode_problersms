def fib_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib_num = fib[-1] + fib[-2]
        fib.append(fib_num)
    return fib
