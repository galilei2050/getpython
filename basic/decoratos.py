import time


def timed(fn):
    def wrapped(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print("work for ", time.time() - start)
        return result
    return wrapped


@timed
def hello_world():
    time.sleep(0.1)
    print("Hello world")


@timed
def sum(x, y):
    return x+y


print("Start program")
hello_world()

print("Summing")
print(sum(10, 1))