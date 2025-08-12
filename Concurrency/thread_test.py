import time
from threading import Thread


def print_hello():
    for i in range(10000000):
        a = 10
        b = 10
        s = a + b


def print_hi():
    for i in range(10000000):
        a = 10
        b = 10
        s = a + b


start_time = time.time()

# t1 = Thread(target=print_hello)
# t2 = Thread(target=print_hi)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
print_hello()
print_hi

end_time = time.time()
print(f"Total runtime: {end_time - start_time:.2f} seconds")
