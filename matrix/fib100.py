# Function to compute the nth Fibonacci number using an iterative approach
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_100_digit():
    n = 478  # The 478th Fibonacci number is the first to have 100 digits
    fib_n = fibonacci(n)  # Get the Fibonacci number
    fib_str = str(fib_n)  # Convert the Fibonacci number to a string
    formatted_fib = "{:,}".format(fib_n)  # Format with commas
    # Return the formatted number and the 100th digit
    return formatted_fib, fib_str[99]


# Output the 100th digit of the Fibonacci number with at least 100 digits
formatted_fib, digit_100 = fibonacci_100_digit()
print("The 478th Fibonacci number (first with 100 digits) is:\n", formatted_fib)
print("\nThe 100th digit of this number is:", digit_100)
