def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):  # Optimized loop range
        if n % i == 0:
            return False
    return True

num = int(input("Number:\n"))
print(isPrime(num))
