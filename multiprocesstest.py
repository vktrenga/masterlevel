import multiprocessing
import time

def compute():
    count = 0
    for i in range(10**2):
        count += i
        print(f"Process {multiprocessing.current_process().name} i: {i}")

if __name__ == "__main__":
    start = time.time()
    processes = [multiprocessing.Process(target=compute) for _ in range(4)]
    for p in processes: p.start()
    for p in processes: p.join()
    print("Multiprocessing time:", time.time() - start)
