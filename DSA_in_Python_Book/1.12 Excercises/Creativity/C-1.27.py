def factors(n):
    k = 1

    while k * k < n:
        if n % k == 0:
            yield k
        k += 1

    while k * k >= 1:
        if n % k == 0:
            yield n // k
        k -= 1


gen = factors(25)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
