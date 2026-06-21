import threading
import time

def compute():
    count = 0
    for i in range(10**2):
        count += i
        print(f"Thread {threading.current_thread().name} count: {i}")


start = time.time()
threads = [threading.Thread(target=compute) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print("Threads time:", time.time() - start)
