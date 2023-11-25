from encrypter import RSA_Encrypter
from decrypter import RSA_Decrypter
from primeFinder import PrimeFinder
from public import PublicKey
from private import PrivateKey
import time
from typing import Optional

def is_coprime(p: int, q: int) -> bool:
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
        
    return p == 1  # If GCD == 1 p and q are coprime

def get_highest_coprime(T: int, N: int) -> Optional[int]:
    nth = 20
    counter = 1
    for number in range(T, 1, -1):
        if is_coprime(T, number):
            if is_coprime(N, number):
                if counter < nth:
                    counter += 1
                else:
                    return number

def get_decryption_number(e: int, T: int) -> int:
    # Run though in sets of SETRANGE numbers to obtain the d number from (e * d) MOD T = 1
    LOOPSTARTPOINT = e - 1
    SETRANGE = 100
    # Loop through from the highest number until a match is found
    while LOOPSTARTPOINT > 1:
        for number in range(LOOPSTARTPOINT, LOOPSTARTPOINT-SETRANGE, -1):
            #print(f'LOOPSTARTPOINT: {LOOPSTARTPOINT}')
            if (e * number) % T == 1:
                return number

        LOOPSTARTPOINT -= SETRANGE

    # If no appropriate number is found
    return 0

def main() -> None:
    start = time.time()
    primeFinder = PrimeFinder(1000)
    p, q = tuple(primeFinder.getRandomPrimes(2))
    print(f"p: {p}", f"q: {q}")
    N = p * q
    print(f"N: {N}")
    T = (p*q) - p - q + 1
    print(f"T: {T}")
    e = get_highest_coprime(T, N)
    if e is None:
        print(f"Failed to find highest coprime of {T} and {N}")
        return
    print(f"e: {e}")
    d = get_decryption_number(e, T)
    end = time.time()
    print(f"d: {d}")
    time_taken = round(end - start, 2)
    print(f"Found all values in {time_taken}s")
    
    public = PublicKey(e, N)
    private = PrivateKey(d, N)
    
    public.encrypt_file("macbeth.txt", "encrypted.txt")
    private.decrypt_file("encrypted.txt", "decrypted.txt")
main()