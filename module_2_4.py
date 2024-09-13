numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i == 1:
        continue
    else:
        is_primes = True
        for j in range(i):
            if j == 0 or j == 1:
                continue
            if i % j == 0:
                is_primes = False
                not_primes.append(i)
                break
        if is_primes:
            primes.append(i)

print(primes)
print(not_primes)