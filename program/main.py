import time
from multiprocessing import Process

def run():
    while True:
        print("running...")
        time.sleep(1)

def main():
    ps = []
    for _ in range(1):
        p = Process(target=run, daemon=True)
        p.start()
        ps.append(p)

    try:
        for p in ps:
            p.join()
    except KeyboardInterrupt:
        print("interrupted")

    print("done")
