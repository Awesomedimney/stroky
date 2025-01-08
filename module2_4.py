numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i % 2 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                primes.append(i)
            elif i == 5:
                primes.append(5)
            else: continue
        elif i == 3:
            primes.append(3)
        else: continue
    elif i == 2:
        primes.append(2)
    else: continue
for i in numbers:
    if i % 2 == 0:
        not_primes.append(i)
    elif i % 3 == 0:
        not_primes.append(i)
    elif i % 5 == 0:
        not_primes.append(i)
    else: continue
not_primes.remove(2)
not_primes.remove(3)
not_primes.remove(5)

print(primes)
print(not_primes)