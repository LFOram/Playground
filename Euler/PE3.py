#he prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def prime(n):
    factors = []
    x = 2
    while n > 1:
        while n % x == 0:
            factors.append(x)
            n /= x
        x = x + 1

    return factors


pfs = prime(600851475143)
print(max(pfs))# The largest element in the prime factor list