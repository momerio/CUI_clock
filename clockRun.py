import datetime
import time
import threading


def schedule(interval, f, wait=True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)


def worker():
    dt_now = datetime.datetime.now()
    print(dt_now.strftime('%H:%M:%S')+"\033[1A")
    time.sleep(1)


dt_now = datetime.datetime.now()
print(dt_now.strftime('%Y年%m月%d日'))

schedule(1, worker, False)
