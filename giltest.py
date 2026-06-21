import threading, time

def io_task(i):
    print(f"Thread {i} starting")
    time.sleep(2)   # GIL released here
    print(f"Thread {i} done")

threads = [threading.Thread(target=io_task, args=(i,)) for i in range(5)]

for t in threads: t.start()
for t in threads: t.join()