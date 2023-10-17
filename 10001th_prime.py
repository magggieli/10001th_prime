import math

def prime(n):
    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

        num += 1

    return primes[-1]

if __name__ == "__main__":
    print(prime(10001))