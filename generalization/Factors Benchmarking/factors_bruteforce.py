import time
import math

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
