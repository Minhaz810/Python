def factors(n):
    results = []

    for i in range(1, n + 1):
        if n % i == 0:
            results.append(i)
        else:
            continue

    return results


f = factors(100)

# print(f)


def factors2(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i


gen = factors2(100)


def factors3(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k + 1


gen2 = factors3(100)

# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))

# generator can efficiently produce infinite numbers


def fibonacci():
    a = 0
    b = 1

    while True:
        yield a
        future = a + b
        a = b
        b = future


fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
