import time
import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def pollards_rho(n):
    def f(x):
        return (x**2 + 1) % n
    
    x = random.randint(2, n - 1)
    y = x
    d = 1
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    
    return d if d != n else None
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 1:
        factor = pollards_rho(n)
        if factor is None:
            factors.append(n)
            break
        while n % factor == 0:
            factors.append(factor)
            n //= factor
    return factors
def benchmark_pollards_rho(n):
    start_time = time.time()
    factors = prime_factors(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return factors, elapsed_time
if __name__ == "__main__":
    n = 384210388873  
    factors, elapsed_time = benchmark_pollards_rho(n)
    print(f"Factors of {n}: {factors}")
    print(f"Time taken for factorization: {elapsed_time:.6f} seconds")


def factors_brute_force(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factors_optimized(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

def factors_prime_product(n):

    factors = [1, n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.extend([i, n // i])
            break  
    return sorted(factors)

def measure_time(function, n):
    start_time = time.time()
    result = function(n)
    elapsed_time = time.time() - start_time
    return result, elapsed_time

if __name__ == "__main__":
    number = 218789674385939  

    print("\n--- Factors using different algorithms ---")
    factors, time_taken = measure_time(factors_brute_force, number)
    print(f"Optimized: {factors}")
    print(f"Time taken: {time_taken:.6f} seconds\n")
    factors, time_taken = measure_time(factors_optimized, number)
    print(f"Optimized: {factors}")
    print(f"Time taken: {time_taken:.6f} seconds\n")
    factors, time_taken = measure_time(factors_prime_product, number)
    print(f"Prime Product Optimized: {factors}")
    print(f"Time taken: {time_taken:.6f} seconds")
    factors, elapsed_time = benchmark_pollards_rho(number)
    print(f"Pollard's Rho of {number}: {factors}")
    print(f"Time taken for factorization: {elapsed_time:.6f} seconds")
