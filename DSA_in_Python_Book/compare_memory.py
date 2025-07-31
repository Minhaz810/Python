import sys

r = range(1_000_000)
l = [i for i in range(1_000_000)]

print(f"range size: {sys.getsizeof(r) / 1024:.2f} KB")
print(f"list size: {sys.getsizeof(l) / 1024:.2f} KB")
