
def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = int(input("Enter a number: "))


start = time.perf_counter()
iterative_result = factorial_iterative(n)
end = time.perf_counter()
iterative_time = end - start

start = time.perf_counter()
recursive_result = factorial_recursive(n)
end = time.perf_counter()
recursive_time = end - start

print("\nFactorial using Iterative Method:", iterative_result)
print("Execution Time (Iterative):", iterative_time, "seconds")

print("\nFactorial using Recursive Method:", recursive_result)
print("Execution Time (Recursive):", recursive_time, "seconds")