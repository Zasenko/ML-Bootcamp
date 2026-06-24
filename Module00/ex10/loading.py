from time import sleep
from time import time


def ft_progress(lst):
    total = len(lst)
    start = time()

    for x in lst:
        current = time()
        elapsed = current - start

        speed = (x + 1) / elapsed
        remaining = total - (x + 1)
        eta = remaining / speed
        percent = int((x + 1) / total * 100)

        bar_len = 20
        filled = int(percent / 100 * bar_len)
        bar = "=" * filled + ">" + " " * (bar_len - filled)

        print(f"ETA: {eta:.2f}s [{percent:3d}%] [{bar}] {x + 1}/{total}"
              f" | elapsed time {elapsed:.2f}s   ", end='\r', flush=True)
        yield x


def main():
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)


if __name__ == "__main__":
    main()
