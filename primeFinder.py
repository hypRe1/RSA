from math import isqrt
import random

class PrimeFinder():
    def __init__(self, upper=50000) -> None:
        if upper < 2:
            print("Upper limit should be greater than 2 if you want to find primes.")
        is_prime = [True] * upper
        is_prime[0] = False
        is_prime[1] = False

        # If you have a composite number then at least one of the two factors needs to be less than
        # the square root of the number
        for index in range(2, isqrt(upper)):
            if is_prime[index]:
                # Use index**2 as previous factors should have been marked out (more efficient)
                for x in range(index*index, upper, index):
                    is_prime[x] = False
        self.primes = [i for i in range(2, upper) if is_prime[i]]
    
    def getRandomPrimes(self, n=2):
        upper_quartile = self.primes[((len(self.primes) // 4) * 3):]
        return (random.choice(upper_quartile) for _ in range(n))
