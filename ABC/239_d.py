a, b, c, d = map(int, input().split())

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i**2, n+1, i):
                primes[j] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]

nums = sieve_of_eratosthenes(200)
win_t = b-a+1
for ab in range(a, b+1):
    for cd in range(c, d+1):
        if ab+cd in nums: 
            win_t -= 1
            break

if win_t <= 0:
    print("Aoki")
else:
    print("Takahashi")
