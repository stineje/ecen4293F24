def fibonacci(n):
    fib_series = [0, 1]  # Starting with F(0) = 0 and F(1) = 1
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series


# Generate the first 10 Fibonacci numbers
n = 15
fib_sequence = fibonacci(n)
print(f"The first {n} Fibonacci numbers are:")
print(fib_sequence)
