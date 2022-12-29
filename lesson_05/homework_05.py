from contextlib import contextmanager

COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
DEFAULT_COLOR = "\033[0m"


@contextmanager
def colorizer(string):
    if string.__eq__("blue"):
        print(COLOR_BLUE, end="")
    if string.__eq__("red"):
        print(COLOR_RED, end="")
    if string.__eq__("green"):
        print(COLOR_GREEN, end="")
    if string.__eq__("yellow"):
        print(COLOR_YELLOW, end="")
    if string.__eq__("default"):
        print(DEFAULT_COLOR, end="")


def frange(start, stop=None, step=None):
    # if set start=0.0 and step = 1.0 if not specified
    start = float(start)
    if stop is None:
        stop = start + 0.0
        start = 0.0
    if step is None:
        step = 1.0

    print("start = ", start, "stop = ", stop, "step = ", step)

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1


assert list(frange(5)) == [0, 1, 2, 3, 4]
assert list(frange(2, 5)) == [2, 3, 4]
assert list(frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(frange(1, 5)) == [1, 2, 3, 4]
assert list(frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(frange(0, 0)) == []
assert list(frange(100, 0)) == []
print("SUCCESS!")

if __name__ == "__main__":
    colorizer("yellow")
    print("hello")
    colorizer("default")
    print("world")
for i in frange(1, 100, 3.5):
    print(i)
