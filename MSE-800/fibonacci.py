def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()  # for a new line after the sequence

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    n = int(input("Enter a number: "))
    fibonacci(n)
    print(f"Factorial of {n} is {factorial(n)}")

if __name__ == "__main__":
    main()