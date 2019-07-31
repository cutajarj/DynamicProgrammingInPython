import time


def countdown(n):
    if n < 0:
        return
    print(n)
    time.sleep(1)
    countdown(n - 1)


countdown(5)
